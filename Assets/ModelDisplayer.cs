using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ModelDisplayer : MonoBehaviour {

	GameObject parent;
	public GameObject prefab;
	GameObject panel;
	GameObject origin;

	GameObject highlights;

	private void Start() {
		highlights = GameObject.Find("Highlights");
		parent = GameObject.Find("Model Spawnpoint");
		panel = GameObject.Find("Info Panel");
		origin = GameObject.Find("Origin");
	}

	public void display() {
		if (parent.transform.childCount == 1)
			Destroy(parent.transform.GetChild(0).gameObject);
		GameObject model;
		if (prefab == null) {
			model = (GameObject)Resources.Load("Models/Ads/" + origin.transform.parent.GetSiblingIndex().ToString());
			//Debug.Log(prefab.name);
		} else {
			model = prefab;
		}
		Debug.Log(parent.name);
		Instantiate(model, parent.transform);
		panel.GetComponent<Canvas>().enabled = true;

		panel.transform.GetChild(3).GetComponent<Text>().text = model.GetComponent<ModelInfo>().info[0];

		panel.transform.GetChild(2).GetComponent<Text>().text = "";
		for (int i = 1; i < model.GetComponent<ModelInfo>().info.Length; i++) {
			panel.transform.GetChild(2).GetComponent<Text>().text += model.GetComponent<ModelInfo>().info[i];
			panel.transform.GetChild(2).GetComponent<Text>().text += "\n";
		}

		for (int i = 0; i < 20; i++) {
			highlights.transform.GetChild(i).GetComponent<Image>().enabled = model.GetComponent<ModelInfo>().station[i];
		}

	}
}
