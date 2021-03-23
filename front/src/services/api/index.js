import requestHandler from "./requestHandler";

const api = {
  ...requestHandler,

  async getAllTasks() {
    return await this.get("/api/tasks");
  },
};

export default api;
