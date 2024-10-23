Instruções de instalação do Python 3.10, criação e ativação de um ambiente virtual (venv), e a instalação dos pacotes **PyOpenGL** e **PyOpenGL_accelerate** usando os arquivos `.whl` (Wheel) que estão dentro da pasta do projeto.

---

# Projeto Exemplo - Setup e Instalação

## Requisitos

- **Windows 64 bits**
- **Powershell**
- **Python 3.10**
  - Se ainda não tem o Python 3.10 instalado, siga os passos abaixo para instalá-lo.

## Instruções de Instalação

### 1. Instalar o Python 3.10

1. Acesse o site oficial do Python e baixe o instalador do Python 3.10:
   - [Baixar Python 3.10](https://www.python.org/downloads/release/python-3100/)

2. Execute o instalador do Python 3.10:
   - Durante a instalação, **marque a opção "Add Python to PATH"**.
   - Siga as instruções da instalação e conclua o processo.

3. Após a instalação, verifique se o Python 3.10 foi instalado corretamente abrindo o **Prompt de Comando** e digitando o seguinte comando:

   ```bash
   # no powershell
   python --version
   ```

   O comando deve retornar algo como:

   ```
   Python 3.10.x
   ```

### 2. Criar um Ambiente Virtual (venv)

1. Abra o **Prompt de Comando**.

2. Navegue até o diretório do projeto onde deseja criar o ambiente virtual. Por exemplo:

   ```bash
   # no powershell
   cd C:\caminho\para\seu\projeto
   ```

3. Crie o ambiente virtual utilizando o Python 3.10 com o seguinte comando:

   ```bash
   # no powershell
   python -m venv venv
   ```

   Isso criará uma nova pasta chamada `venv` no seu diretório de projeto.

### 3. Ativar o Ambiente Virtual

1. Ative o ambiente virtual com o seguinte comando:

   - **Windows**:

     ```bash
     # no powershell
     venv\Scripts\activate
     ```

2. Após ativar o ambiente virtual, o prompt de comando deve mostrar o nome do ambiente, indicando que ele está ativo. O prompt deve mudar para algo assim:

   ```
   (venv) C:\caminho\para\seu\projeto>
   ```

### 4. Instalar PyOpenGL e PyOpenGL_accelerate

Os arquivos de instalação `PyOpenGL-3.1.7-cp310-cp310-win_amd64.whl` e `PyOpenGL_accelerate-3.1.7-cp310-cp310-win_amd64.whl` já estão dentro da pasta do projeto. Entre na pasta projeto `cd .\projeto\` e agora, vamos instalar esses pacotes.

1. Com o ambiente virtual ativo, use os comandos abaixo para instalar os pacotes:

   - Instalar **PyOpenGL**:

     ```bash
     pip install PyOpenGL-3.1.7-cp310-cp310-win_amd64.whl
     ```

   - Instalar **PyOpenGL_accelerate**:

     ```bash
     pip install PyOpenGL_accelerate-3.1.7-cp310-cp310-win_amd64.whl
     ```

2. Após a instalação, você pode verificar se tudo foi instalado corretamente com:

   ```bash
   pip list
   ```

   Isso mostrará uma lista de pacotes instalados, onde você deverá ver o **PyOpenGL 3.1.7** e **PyOpenGL_accelerate 3.1.7**.

### 5. Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual usando o comando:

```bash
deactivate
```

Isso retornará o prompt ao seu estado normal, fora do ambiente virtual.

---

## Resumo dos Comandos

1. **Instalar Python 3.10**:
   - Baixar e instalar Python 3.10 a partir do site oficial.
   - Verificar a instalação com:

     ```bash
     python --version
     ```

2. **Criar e ativar o ambiente virtual**:
   - Criar o ambiente virtual com Python 3.10:

     ```bash
     python -m venv venv
     ```

   - Ativar o ambiente virtual:

     ```bash
     venv\Scripts\activate
     ```

3. **Instalar PyOpenGL e PyOpenGL_accelerate**:

   - Entrar pasta na **projeto**:

     ```bash
     cd .\projeto\        
     ```

   - Instalar o **PyOpenGL**:

     ```bash
     pip install PyOpenGL-3.1.7-cp310-cp310-win_amd64.whl
     ```

   - Instalar o **PyOpenGL_accelerate**:

     ```bash
     pip install PyOpenGL_accelerate-3.1.7-cp310-cp310-win_amd64.whl
     ```

4. **Desativar o ambiente virtual**:

   ```bash
   deactivate
   ```

---

Com essas instruções, você terá o Python 3.10 instalado, o ambiente virtual configurado, e as bibliotecas PyOpenGL e PyOpenGL_accelerate instaladas corretamente no ambiente de desenvolvimento.