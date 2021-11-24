def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 5092, "metric_value": 0.9835, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 3688, "metric_value": 0.9506, "depth": 2}
		if obj[6]<=0:
			# {"feature": "Coffeehouse", "instances": 1849, "metric_value": 0.8497, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Driving_to", "instances": 1377, "metric_value": 0.7932, "depth": 4}
				if obj[0]<=0:
					# {"feature": "Time", "instances": 753, "metric_value": 0.7177, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Education", "instances": 444, "metric_value": 0.6448, "depth": 6}
						if obj[11]<=3:
							# {"feature": "Passanger", "instances": 415, "metric_value": 0.671, "depth": 7}
							if obj[1]>1:
								# {"feature": "Bar", "instances": 336, "metric_value": 0.7267, "depth": 8}
								if obj[14]>0.0:
									# {"feature": "Occupation", "instances": 220, "metric_value": 0.6535, "depth": 9}
									if obj[12]<=7.704545454545454:
										# {"feature": "Income", "instances": 132, "metric_value": 0.5328, "depth": 10}
										if obj[13]<=6:
											# {"feature": "Maritalstatus", "instances": 105, "metric_value": 0.422, "depth": 11}
											if obj[9]<=0:
												# {"feature": "Children", "instances": 55, "metric_value": 0.5983, "depth": 12}
												if obj[10]>0:
													# {"feature": "Carryaway", "instances": 39, "metric_value": 0.4771, "depth": 13}
													if obj[16]>2.0:
														# {"feature": "Weather", "instances": 22, "metric_value": 0.684, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.5917, "depth": 15}
															if obj[18]<=2.0:
																# {"feature": "Age", "instances": 15, "metric_value": 0.3534, "depth": 16}
																if obj[8]<=3:
																	return 'True'
																elif obj[8]>3:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]>55:
																		return 'False'
																	elif obj[3]<=55:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[18]>2.0:
																# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[8]<=0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=3.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[8]>0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=4.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'False'
														else: return 'False'
													elif obj[16]<=2.0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0:
													# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 13}
													if obj[18]>1.0:
														# {"feature": "Carryaway", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[16]>2.0:
															return 'True'
														elif obj[16]<=2.0:
															# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[3]>55:
																return 'True'
															elif obj[3]<=55:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[18]<=1.0:
														# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[17]<=3.0:
															# {"feature": "Carryaway", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[16]>3.0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[8]<=0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[16]<=3.0:
																return 'False'
															else: return 'False'
														elif obj[17]>3.0:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											elif obj[9]>0:
												# {"feature": "Restaurant20to50", "instances": 50, "metric_value": 0.1414, "depth": 12}
												if obj[18]>0.0:
													return 'True'
												elif obj[18]<=0.0:
													# {"feature": "Carryaway", "instances": 10, "metric_value": 0.469, "depth": 13}
													if obj[16]>2.0:
														return 'True'
													elif obj[16]<=2.0:
														# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[3]>55:
															return 'True'
														elif obj[3]<=55:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[13]>6:
											# {"feature": "Restaurantlessthan20", "instances": 27, "metric_value": 0.8256, "depth": 11}
											if obj[17]<=2.0:
												# {"feature": "Age", "instances": 18, "metric_value": 0.9641, "depth": 12}
												if obj[8]>1:
													# {"feature": "Weather", "instances": 11, "metric_value": 0.9457, "depth": 13}
													if obj[2]<=0:
														# {"feature": "Carryaway", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[16]>2.0:
															# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[3]>55:
																return 'True'
															elif obj[3]<=55:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]>0:
																		return 'True'
																	elif obj[10]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[7]>0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[16]<=2.0:
															return 'False'
														else: return 'False'
													elif obj[2]>0:
														return 'False'
													else: return 'False'
												elif obj[8]<=1:
													return 'True'
												else: return 'True'
											elif obj[17]>2.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[12]>7.704545454545454:
										# {"feature": "Income", "instances": 88, "metric_value": 0.7928, "depth": 10}
										if obj[13]<=6:
											# {"feature": "Carryaway", "instances": 79, "metric_value": 0.8354, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.669, "depth": 12}
												if obj[18]<=1.0:
													# {"feature": "Age", "instances": 21, "metric_value": 0.2762, "depth": 13}
													if obj[8]<=3:
														return 'True'
													elif obj[8]>3:
														# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[20]>1:
															return 'True'
														elif obj[20]<=1:
															# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[17]>2.0:
																return 'True'
															elif obj[17]<=2.0:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[18]>1.0:
													# {"feature": "Age", "instances": 19, "metric_value": 0.8997, "depth": 13}
													if obj[8]>0:
														# {"feature": "Maritalstatus", "instances": 14, "metric_value": 0.7496, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.8113, "depth": 15}
															if obj[17]>2.0:
																# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 16}
																if obj[20]>1:
																	return 'True'
																elif obj[20]<=1:
																	return 'False'
																else: return 'False'
															elif obj[17]<=2.0:
																# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[3]>55:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[3]<=55:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[9]>1:
															return 'True'
														else: return 'True'
													elif obj[8]<=0:
														# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[2]>0:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															elif obj[2]<=0:
																return 'True'
															else: return 'True'
														elif obj[9]>1:
															return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]<=2.0:
												# {"feature": "Age", "instances": 39, "metric_value": 0.9418, "depth": 12}
												if obj[8]<=3:
													# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.874, "depth": 13}
													if obj[18]>0.0:
														# {"feature": "Children", "instances": 32, "metric_value": 0.8113, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.5033, "depth": 15}
															if obj[17]<=2.0:
																# {"feature": "Weather", "instances": 12, "metric_value": 0.65, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.7219, "depth": 17}
																	if obj[9]>0:
																		# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[3]>55:
																			return 'True'
																		elif obj[3]<=55:
																			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[7]<=0:
																				return 'True'
																			elif obj[7]>0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[9]<=0:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[2]>0:
																	return 'True'
																else: return 'True'
															elif obj[17]>2.0:
																return 'True'
															else: return 'True'
														elif obj[10]>0:
															# {"feature": "Temperature", "instances": 14, "metric_value": 0.9852, "depth": 15}
															if obj[3]>55:
																# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 16}
																if obj[17]<=2.0:
																	# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=2:
																		# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[20]<=1:
																			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[20]>1:
																			return 'False'
																		else: return 'False'
																	elif obj[9]>2:
																		return 'True'
																	else: return 'True'
																elif obj[17]>2.0:
																	return 'False'
																else: return 'False'
															elif obj[3]<=55:
																# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[9]<=1:
																	return 'True'
																elif obj[9]>1:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]>0:
																		return 'False'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'True'
														else: return 'True'
													elif obj[18]<=0.0:
														return 'False'
													else: return 'False'
												elif obj[8]>3:
													# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[9]<=0:
														return 'False'
													elif obj[9]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[13]>6:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[14]<=0.0:
									# {"feature": "Occupation", "instances": 116, "metric_value": 0.8375, "depth": 9}
									if obj[12]>1:
										# {"feature": "Age", "instances": 98, "metric_value": 0.8886, "depth": 10}
										if obj[8]>0:
											# {"feature": "Gender", "instances": 91, "metric_value": 0.8482, "depth": 11}
											if obj[7]>0:
												# {"feature": "Carryaway", "instances": 54, "metric_value": 0.9357, "depth": 12}
												if obj[16]<=3.0:
													# {"feature": "Restaurantlessthan20", "instances": 44, "metric_value": 0.9024, "depth": 13}
													if obj[17]<=2.0:
														# {"feature": "Income", "instances": 35, "metric_value": 0.9518, "depth": 14}
														if obj[13]>0:
															# {"feature": "Maritalstatus", "instances": 33, "metric_value": 0.9183, "depth": 15}
															if obj[9]>0:
																# {"feature": "Weather", "instances": 23, "metric_value": 0.9877, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Temperature", "instances": 22, "metric_value": 0.994, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Children", "instances": 11, "metric_value": 0.9457, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 19}
																			if obj[20]>1:
																				return 'True'
																			elif obj[20]<=1:
																				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[18]<=0.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[18]>0.0:
																					return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[18]>0.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[18]<=0.0:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[3]>55:
																		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 18}
																		if obj[18]>0.0:
																			# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[10]>0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[18]<=0.0:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																elif obj[2]>0:
																	return 'True'
																else: return 'True'
															elif obj[9]<=0:
																# {"feature": "Temperature", "instances": 10, "metric_value": 0.469, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 19}
																			if obj[18]<=1.0:
																				# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[13]<=0:
															return 'False'
														else: return 'False'
													elif obj[17]>2.0:
														# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[18]>0.0:
															return 'True'
														elif obj[18]<=0.0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[16]>3.0:
													# {"feature": "Temperature", "instances": 10, "metric_value": 1.0, "depth": 13}
													if obj[3]>55:
														# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9]>0:
															return 'True'
														elif obj[9]<=0:
															# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[20]>1:
																return 'False'
															elif obj[20]<=1:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[3]<=55:
														# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[13]<=4:
															return 'False'
														elif obj[13]>4:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'False'
											elif obj[7]<=0:
												# {"feature": "Maritalstatus", "instances": 37, "metric_value": 0.6395, "depth": 12}
												if obj[9]<=1:
													# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.5813, "depth": 13}
													if obj[17]>1.0:
														# {"feature": "Income", "instances": 28, "metric_value": 0.6769, "depth": 14}
														if obj[13]<=6:
															# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.7919, "depth": 15}
															if obj[18]>0.0:
																# {"feature": "Weather", "instances": 18, "metric_value": 0.8524, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Carryaway", "instances": 17, "metric_value": 0.874, "depth": 17}
																	if obj[16]>0.0:
																		# {"feature": "Temperature", "instances": 16, "metric_value": 0.896, "depth": 18}
																		if obj[3]>55:
																			# {"feature": "Children", "instances": 12, "metric_value": 0.9183, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 20}
																				if obj[20]>1:
																					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[20]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[10]>0:
																				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[20]<=1:
																					return 'True'
																				elif obj[20]>1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'True'
																		elif obj[3]<=55:
																			# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[10]>0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]<=0:
																				return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[16]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[2]>0:
																	return 'True'
																else: return 'True'
															elif obj[18]<=0.0:
																return 'True'
															else: return 'True'
														elif obj[13]>6:
															return 'True'
														else: return 'True'
													elif obj[17]<=1.0:
														return 'True'
													else: return 'True'
												elif obj[9]>1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]<=0:
											# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[17]<=2.0:
												return 'False'
											elif obj[17]>2.0:
												# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9]<=0:
													return 'True'
												elif obj[9]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'False'
									elif obj[12]<=1:
										# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.3095, "depth": 10}
										if obj[17]>1.0:
											return 'True'
										elif obj[17]<=1.0:
											# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[3]>55:
												# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[7]>0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[20]<=1:
														return 'True'
													elif obj[20]>1:
														return 'False'
													else: return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											elif obj[3]<=55:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=1:
								# {"feature": "Occupation", "instances": 79, "metric_value": 0.3404, "depth": 8}
								if obj[12]>1:
									# {"feature": "Maritalstatus", "instances": 70, "metric_value": 0.1872, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Restaurant20to50", "instances": 68, "metric_value": 0.1106, "depth": 10}
										if obj[18]>0.0:
											return 'True'
										elif obj[18]<=0.0:
											# {"feature": "Carryaway", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[16]<=2.0:
												return 'True'
											elif obj[16]>2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>2:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=2:
											return 'True'
										elif obj[8]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=1:
									# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[10]>0:
										# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[18]>0.0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8]<=3:
												return 'False'
											elif obj[8]>3:
												# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[13]>3:
													return 'False'
												elif obj[13]<=3:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[18]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[10]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[11]>3:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						# {"feature": "Bar", "instances": 309, "metric_value": 0.8048, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Income", "instances": 197, "metric_value": 0.8868, "depth": 7}
							if obj[13]<=4:
								# {"feature": "Carryaway", "instances": 132, "metric_value": 0.7309, "depth": 8}
								if obj[16]>2.0:
									# {"feature": "Occupation", "instances": 75, "metric_value": 0.5294, "depth": 9}
									if obj[12]>5:
										# {"feature": "Education", "instances": 41, "metric_value": 0.7593, "depth": 10}
										if obj[11]>0:
											# {"feature": "Maritalstatus", "instances": 27, "metric_value": 0.9183, "depth": 11}
											if obj[9]>0:
												# {"feature": "Passanger", "instances": 20, "metric_value": 0.8113, "depth": 12}
												if obj[1]>0:
													# {"feature": "Temperature", "instances": 15, "metric_value": 0.9183, "depth": 13}
													if obj[3]<=55:
														# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[2]<=1:
															return 'True'
														elif obj[2]>1:
															# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[8]>2:
																return 'False'
															elif obj[8]<=2:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[3]>55:
														# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[17]<=3.0:
															# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[8]<=4:
																return 'False'
															elif obj[8]>4:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=2.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[17]>3.0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0:
												# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[1]<=0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[20]>1:
															return 'False'
														elif obj[20]<=1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[1]>0:
													# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[2]<=0:
														return 'True'
													elif obj[2]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[11]<=0:
											return 'True'
										else: return 'True'
									elif obj[12]<=5:
										return 'True'
									else: return 'True'
								elif obj[16]<=2.0:
									# {"feature": "Temperature", "instances": 57, "metric_value": 0.8997, "depth": 9}
									if obj[3]>55:
										# {"feature": "Education", "instances": 31, "metric_value": 0.9812, "depth": 10}
										if obj[11]<=3:
											# {"feature": "Children", "instances": 27, "metric_value": 0.999, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.9495, "depth": 12}
												if obj[9]>1:
													# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 13}
													if obj[18]<=1.0:
														# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[20]>1:
															return 'True'
														elif obj[20]<=1:
															# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[12]<=6:
																return 'False'
															elif obj[12]>6:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[18]>1.0:
														return 'False'
													else: return 'False'
												elif obj[9]<=1:
													# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[8]<=4:
														return 'True'
													elif obj[8]>4:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[10]>0:
												# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[12]>1:
														return 'False'
													elif obj[12]<=1:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[20]<=1:
															return 'True'
														elif obj[20]>1:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[1]>2:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[11]>3:
											return 'True'
										else: return 'True'
									elif obj[3]<=55:
										# {"feature": "Age", "instances": 26, "metric_value": 0.7063, "depth": 10}
										if obj[8]<=3:
											# {"feature": "Weather", "instances": 17, "metric_value": 0.874, "depth": 11}
											if obj[2]>0:
												# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 12}
												if obj[18]<=1.0:
													# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[12]<=12:
														return 'True'
													elif obj[12]>12:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]>1:
															return 'False'
														elif obj[1]<=1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[18]>1.0:
													# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[11]<=4:
														return 'False'
													elif obj[11]>4:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[2]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]>3:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[13]>4:
								# {"feature": "Restaurant20to50", "instances": 65, "metric_value": 0.9998, "depth": 8}
								if obj[18]>1.0:
									# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.9183, "depth": 9}
									if obj[17]<=3.0:
										# {"feature": "Maritalstatus", "instances": 31, "metric_value": 0.9629, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Age", "instances": 18, "metric_value": 0.8524, "depth": 11}
											if obj[8]<=6:
												# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 12}
												if obj[11]>1:
													return 'True'
												elif obj[11]<=1:
													# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[12]>1:
														# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[1]>1:
															# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]>30:
																	return 'True'
																elif obj[3]<=30:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														elif obj[1]<=1:
															return 'False'
														else: return 'False'
													elif obj[12]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>6:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]<=3:
													# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[2]<=2:
														# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[3]<=30:
															# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[10]<=1:
																	# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[11]<=3:
																		# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[12]<=12:
																			# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[16]<=2.0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>0:
											# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[12]>4:
													return 'False'
												elif obj[12]<=4:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=80:
																# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[8]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=3.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'False'
														else: return 'False'
													elif obj[7]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[17]>3.0:
										return 'True'
									else: return 'True'
								elif obj[18]<=1.0:
									# {"feature": "Passanger", "instances": 29, "metric_value": 0.8498, "depth": 9}
									if obj[1]>0:
										# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 10}
										if obj[11]>1:
											# {"feature": "Carryaway", "instances": 20, "metric_value": 0.8113, "depth": 11}
											if obj[16]>1.0:
												# {"feature": "Age", "instances": 12, "metric_value": 0.9799, "depth": 12}
												if obj[8]>1:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 13}
													if obj[7]>0:
														# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 14}
														if obj[2]>0:
															# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[12]<=6:
																return 'False'
															elif obj[12]>6:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=30:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=3.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[2]<=0:
															# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[9]<=0:
																return 'True'
															elif obj[9]>0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]>30:
																	return 'False'
																elif obj[3]<=30:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													elif obj[7]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]<=1:
													return 'True'
												else: return 'True'
											elif obj[16]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[11]<=1:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[14]<=0.0:
							# {"feature": "Age", "instances": 112, "metric_value": 0.5917, "depth": 7}
							if obj[8]>0:
								# {"feature": "Occupation", "instances": 86, "metric_value": 0.3651, "depth": 8}
								if obj[12]<=7:
									# {"feature": "Carryaway", "instances": 55, "metric_value": 0.4972, "depth": 9}
									if obj[16]<=3.0:
										# {"feature": "Maritalstatus", "instances": 53, "metric_value": 0.4508, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Restaurantlessthan20", "instances": 33, "metric_value": 0.6136, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Passanger", "instances": 30, "metric_value": 0.469, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Income", "instances": 18, "metric_value": 0.65, "depth": 13}
													if obj[13]<=6:
														# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[18]<=1.0:
															return 'True'
														elif obj[18]>1.0:
															# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[11]<=1:
																return 'True'
															elif obj[11]>1:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													elif obj[13]>6:
														# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[3]>30:
															# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]>0:
																	return 'True'
																elif obj[7]<=0:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'False'
															else: return 'False'
														elif obj[3]<=30:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[1]>1:
													return 'True'
												else: return 'True'
											elif obj[17]<=1.0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]>1:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									elif obj[16]>3.0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]>1:
											return 'False'
										elif obj[1]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[12]>7:
									return 'True'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Income", "instances": 26, "metric_value": 0.9612, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Weather", "instances": 18, "metric_value": 0.9911, "depth": 9}
									if obj[2]<=0:
										# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 10}
										if obj[12]<=7:
											# {"feature": "Education", "instances": 12, "metric_value": 1.0, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[7]>0:
													# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[1]>1:
														# {"feature": "Carryaway", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[16]>2.0:
															# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[3]>30:
																# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[18]>0.0:
																		return 'False'
																	elif obj[18]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[9]>0:
																	return 'True'
																else: return 'True'
															elif obj[3]<=30:
																return 'True'
															else: return 'True'
														elif obj[16]<=2.0:
															return 'False'
														else: return 'False'
													elif obj[1]<=1:
														return 'False'
													else: return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											elif obj[11]>2:
												# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[20]<=1:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=1:
														return 'False'
													elif obj[1]>1:
														return 'True'
													else: return 'True'
												elif obj[20]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[12]>7:
											return 'True'
										else: return 'True'
									elif obj[2]>0:
										return 'False'
									else: return 'False'
								elif obj[13]>4:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>0:
					# {"feature": "Distance", "instances": 624, "metric_value": 0.8667, "depth": 5}
					if obj[20]<=1:
						# {"feature": "Carryaway", "instances": 417, "metric_value": 0.8026, "depth": 6}
						if obj[16]>1.0:
							# {"feature": "Age", "instances": 356, "metric_value": 0.7533, "depth": 7}
							if obj[8]>0:
								# {"feature": "Income", "instances": 302, "metric_value": 0.7126, "depth": 8}
								if obj[13]<=6:
									# {"feature": "Weather", "instances": 241, "metric_value": 0.6484, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Restaurantlessthan20", "instances": 231, "metric_value": 0.6649, "depth": 10}
										if obj[17]<=3.0:
											# {"feature": "Time", "instances": 202, "metric_value": 0.6184, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Occupation", "instances": 173, "metric_value": 0.5496, "depth": 12}
												if obj[12]>2:
													# {"feature": "Children", "instances": 139, "metric_value": 0.4481, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Education", "instances": 83, "metric_value": 0.5961, "depth": 14}
														if obj[11]<=1:
															# {"feature": "Direction_same", "instances": 42, "metric_value": 0.3712, "depth": 15}
															if obj[19]<=0:
																# {"feature": "Gender", "instances": 22, "metric_value": 0.5746, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 17}
																	if obj[14]<=1.0:
																		# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[9]<=1:
																			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[18]<=1.0:
																				# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[3]>30:
																					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[1]<=1:
																						return 'False'
																					else: return 'False'
																				elif obj[3]<=30:
																					return 'False'
																				else: return 'False'
																			elif obj[18]>1.0:
																				return 'True'
																			else: return 'True'
																		elif obj[9]>1:
																			return 'True'
																		else: return 'True'
																	elif obj[14]>1.0:
																		return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	return 'True'
																else: return 'True'
															elif obj[19]>0:
																return 'True'
															else: return 'True'
														elif obj[11]>1:
															# {"feature": "Maritalstatus", "instances": 41, "metric_value": 0.7593, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Direction_same", "instances": 25, "metric_value": 0.5294, "depth": 16}
																if obj[19]>0:
																	return 'True'
																elif obj[19]<=0:
																	# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 17}
																	if obj[18]<=1.0:
																		# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 18}
																		if obj[14]<=1.0:
																			# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=55:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[14]>1.0:
																			return 'True'
																		else: return 'True'
																	elif obj[18]>1.0:
																		# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[7]<=0:
																					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[14]<=2.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[9]>1:
																# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9544, "depth": 16}
																if obj[19]>0:
																	# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 1.0, "depth": 17}
																	if obj[18]>0.0:
																		# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 18}
																		if obj[14]<=2.0:
																			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 19}
																			if obj[1]>0:
																				# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[3]<=80:
																						return 'True'
																					else: return 'True'
																				elif obj[7]<=0:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=80:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[1]<=0:
																				return 'True'
																			else: return 'True'
																		elif obj[14]>2.0:
																			return 'False'
																		else: return 'False'
																	elif obj[18]<=0.0:
																		return 'False'
																	else: return 'False'
																elif obj[19]<=0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[10]>0:
														# {"feature": "Temperature", "instances": 56, "metric_value": 0.1292, "depth": 14}
														if obj[3]>30:
															return 'True'
														elif obj[3]<=30:
															# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[18]>0.0:
																return 'True'
															elif obj[18]<=0.0:
																# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[11]>0:
																	return 'False'
																elif obj[11]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[12]<=2:
													# {"feature": "Bar", "instances": 34, "metric_value": 0.8338, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Passanger", "instances": 26, "metric_value": 0.9306, "depth": 14}
														if obj[1]>0:
															# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9656, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9852, "depth": 16}
																if obj[19]>0:
																	# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 17}
																	if obj[18]>0.0:
																		# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[3]<=80:
																						return 'True'
																					else: return 'True'
																				elif obj[10]<=0:
																					# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[3]<=80:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]<=0:
																				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=80:
																						return 'True'
																					else: return 'True'
																				elif obj[10]>0:
																					return 'False'
																				else: return 'False'
																			else: return 'True'
																		elif obj[11]>2:
																			return 'True'
																		else: return 'True'
																	elif obj[18]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[19]<=0:
																	# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 17}
																	if obj[18]>0.0:
																		return 'False'
																	elif obj[18]<=0.0:
																		# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[3]<=55:
																			return 'True'
																		elif obj[3]>55:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																else: return 'False'
															elif obj[9]>1:
																return 'True'
															else: return 'True'
														elif obj[1]<=0:
															return 'True'
														else: return 'True'
													elif obj[14]>1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>1:
												# {"feature": "Occupation", "instances": 29, "metric_value": 0.8936, "depth": 12}
												if obj[12]<=7:
													# {"feature": "Passanger", "instances": 20, "metric_value": 0.6098, "depth": 13}
													if obj[1]>0:
														# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.4855, "depth": 14}
														if obj[9]<=2:
															# {"feature": "Bar", "instances": 17, "metric_value": 0.3228, "depth": 15}
															if obj[14]<=1.0:
																return 'True'
															elif obj[14]>1.0:
																# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[11]<=2:
																	# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[18]<=0.0:
																		return 'True'
																	elif obj[18]>0.0:
																		return 'False'
																	else: return 'False'
																elif obj[11]>2:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[9]>2:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=0:
																return 'True'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[1]<=0:
														return 'False'
													else: return 'False'
												elif obj[12]>7:
													# {"feature": "Temperature", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[3]>55:
														# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[11]>0:
															# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[19]>0:
																return 'False'
															elif obj[19]<=0:
																return 'True'
															else: return 'True'
														elif obj[11]<=0:
															return 'True'
														else: return 'True'
													elif obj[3]<=55:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[17]>3.0:
											# {"feature": "Maritalstatus", "instances": 29, "metric_value": 0.8936, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.684, "depth": 12}
												if obj[18]>1.0:
													# {"feature": "Children", "instances": 15, "metric_value": 0.3534, "depth": 13}
													if obj[10]<=0:
														return 'True'
													elif obj[10]>0:
														# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[3]>55:
															return 'True'
														elif obj[3]<=55:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]>0:
																return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[18]<=1.0:
													# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[4]<=1:
															# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[12]<=10:
																return 'False'
															elif obj[12]>10:
																return 'True'
															else: return 'True'
														elif obj[4]>1:
															return 'True'
														else: return 'True'
													elif obj[10]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]>1:
												# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[3]>55:
													return 'False'
												elif obj[3]<=55:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[2]>1:
										return 'True'
									else: return 'True'
								elif obj[13]>6:
									# {"feature": "Weather", "instances": 61, "metric_value": 0.8949, "depth": 9}
									if obj[2]<=0:
										# {"feature": "Restaurantlessthan20", "instances": 50, "metric_value": 0.8267, "depth": 10}
										if obj[17]<=3.0:
											# {"feature": "Bar", "instances": 43, "metric_value": 0.8841, "depth": 11}
											if obj[14]>0.0:
												# {"feature": "Occupation", "instances": 31, "metric_value": 0.9629, "depth": 12}
												if obj[12]<=12:
													# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 13}
													if obj[11]<=1:
														# {"feature": "Gender", "instances": 15, "metric_value": 0.8366, "depth": 14}
														if obj[7]<=0:
															# {"feature": "Passanger", "instances": 11, "metric_value": 0.9457, "depth": 15}
															if obj[1]>0:
																# {"feature": "Temperature", "instances": 10, "metric_value": 0.8813, "depth": 16}
																if obj[3]>30:
																	# {"feature": "Time", "instances": 9, "metric_value": 0.9183, "depth": 17}
																	if obj[4]<=1:
																		# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[18]>0.0:
																			# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[19]>0:
																						return 'True'
																					elif obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[9]>1:
																				return 'True'
																			else: return 'True'
																		elif obj[18]<=0.0:
																			return 'False'
																		else: return 'False'
																	elif obj[4]>1:
																		return 'True'
																	else: return 'True'
																elif obj[3]<=30:
																	return 'True'
																else: return 'True'
															elif obj[1]<=0:
																return 'False'
															else: return 'False'
														elif obj[7]>0:
															return 'True'
														else: return 'True'
													elif obj[11]>1:
														# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9612, "depth": 14}
														if obj[18]<=1.0:
															# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[4]<=1:
																return 'False'
															elif obj[4]>1:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	return 'True'
																elif obj[7]<=0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[18]>1.0:
															# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[9]>0:
																# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[4]>0:
																	return 'True'
																elif obj[4]<=0:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[19]>0:
																		return 'True'
																	elif obj[19]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[9]<=0:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'False'
												elif obj[12]>12:
													return 'True'
												else: return 'True'
											elif obj[14]<=0.0:
												# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.4138, "depth": 12}
												if obj[9]>0:
													return 'True'
												elif obj[9]<=0:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]>55:
														return 'False'
													elif obj[3]<=55:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[17]>3.0:
											return 'True'
										else: return 'True'
									elif obj[2]>0:
										# {"feature": "Temperature", "instances": 11, "metric_value": 0.994, "depth": 10}
										if obj[3]>30:
											# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[18]<=1.0:
												# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[1]>0:
													# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[12]>6:
														# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[7]<=0:
															return 'False'
														elif obj[7]>0:
															# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11]<=0:
																return 'True'
															elif obj[11]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[12]<=6:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[18]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[8]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 54, "metric_value": 0.9183, "depth": 8}
								if obj[17]<=3.0:
									# {"feature": "Occupation", "instances": 46, "metric_value": 0.9656, "depth": 9}
									if obj[12]>2:
										# {"feature": "Income", "instances": 33, "metric_value": 0.9993, "depth": 10}
										if obj[13]<=5:
											# {"feature": "Education", "instances": 27, "metric_value": 0.9911, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Weather", "instances": 20, "metric_value": 0.9928, "depth": 12}
												if obj[2]<=1:
													# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9641, "depth": 13}
													if obj[19]>0:
														# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 14}
														if obj[7]>0:
															# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 15}
															if obj[9]<=0:
																# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[3]>30:
																	# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[1]>0:
																		# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[4]<=1:
																			return 'True'
																		elif obj[4]>1:
																			return 'False'
																		else: return 'False'
																	elif obj[1]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[3]<=30:
																	return 'True'
																else: return 'True'
															elif obj[9]>0:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													elif obj[19]<=0:
														# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[10]<=0:
															return 'False'
														elif obj[10]>0:
															# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14]<=0.0:
																	return 'False'
																elif obj[14]>0.0:
																	return 'True'
																else: return 'True'
															elif obj[7]>0:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[2]>1:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[9]<=1:
													return 'False'
												elif obj[9]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[13]>5:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[18]<=1.0:
												return 'True'
											elif obj[18]>1.0:
												# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[2]>0:
													return 'True'
												elif obj[2]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[12]<=2:
										# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.6194, "depth": 10}
										if obj[9]<=0:
											return 'True'
										elif obj[9]>0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4]>0:
												return 'False'
											elif obj[4]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[17]>3.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[16]<=1.0:
							# {"feature": "Children", "instances": 61, "metric_value": 0.9764, "depth": 7}
							if obj[10]>0:
								# {"feature": "Time", "instances": 32, "metric_value": 0.8571, "depth": 8}
								if obj[4]>0:
									# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.4855, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Income", "instances": 18, "metric_value": 0.3095, "depth": 10}
										if obj[13]>1:
											return 'True'
										elif obj[13]<=1:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[14]>0.0:
												return 'True'
											elif obj[14]<=0.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[13]<=7:
										# {"feature": "Temperature", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[3]>30:
											# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[8]<=2:
												# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[12]>1:
													# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[11]>3:
														# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[19]<=0:
															return 'False'
														elif obj[19]>0:
															return 'True'
														else: return 'True'
													elif obj[11]<=3:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]>2:
												return 'False'
											else: return 'False'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									elif obj[13]>7:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[10]<=0:
								# {"feature": "Temperature", "instances": 29, "metric_value": 0.9923, "depth": 8}
								if obj[3]>55:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.8997, "depth": 9}
									if obj[19]>0:
										# {"feature": "Age", "instances": 16, "metric_value": 0.9544, "depth": 10}
										if obj[8]<=5:
											# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.9183, "depth": 11}
											if obj[9]>0:
												# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 12}
												if obj[4]<=0:
													return 'False'
												elif obj[4]>0:
													# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[17]>1.0:
														return 'False'
													elif obj[17]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[9]<=0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[1]>0:
													# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[4]>0:
														# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=1:
															return 'False'
														elif obj[12]>1:
															return 'True'
														else: return 'True'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[8]>5:
											return 'True'
										else: return 'True'
									elif obj[19]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]<=55:
									# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[12]>7:
										# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[7]<=0:
											# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[8]>2:
												return 'True'
											elif obj[8]<=2:
												# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[2]<=1:
													return 'False'
												elif obj[2]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[7]>0:
											return 'False'
										else: return 'False'
									elif obj[12]<=7:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[20]>1:
						# {"feature": "Time", "instances": 207, "metric_value": 0.9558, "depth": 6}
						if obj[4]<=1:
							# {"feature": "Occupation", "instances": 183, "metric_value": 0.9764, "depth": 7}
							if obj[12]<=6.994535519125683:
								# {"feature": "Education", "instances": 100, "metric_value": 0.9248, "depth": 8}
								if obj[11]<=4:
									# {"feature": "Age", "instances": 98, "metric_value": 0.9113, "depth": 9}
									if obj[8]>1:
										# {"feature": "Income", "instances": 61, "metric_value": 0.967, "depth": 10}
										if obj[13]<=4:
											# {"feature": "Carryaway", "instances": 49, "metric_value": 0.9925, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.9044, "depth": 12}
												if obj[18]>0.0:
													# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9587, "depth": 13}
													if obj[19]<=0:
														# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.9975, "depth": 14}
														if obj[17]>1.0:
															# {"feature": "Bar", "instances": 16, "metric_value": 1.0, "depth": 15}
															if obj[14]>0.0:
																# {"feature": "Weather", "instances": 14, "metric_value": 0.9852, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Maritalstatus", "instances": 12, "metric_value": 1.0, "depth": 17}
																	if obj[9]>0:
																		# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 19}
																			if obj[3]>55:
																				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[1]<=1:
																						return 'False'
																					else: return 'False'
																				elif obj[10]<=0:
																					return 'True'
																				else: return 'True'
																			elif obj[3]<=55:
																				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[1]<=1:
																						return 'False'
																					else: return 'False'
																				elif obj[10]<=0:
																					return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[7]<=0:
																			# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[3]>55:
																				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[3]<=55:
																				return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[9]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[2]>0:
																	return 'True'
																else: return 'True'
															elif obj[14]<=0.0:
																return 'False'
															else: return 'False'
														elif obj[17]<=1.0:
															return 'True'
														else: return 'True'
													elif obj[19]>0:
														return 'True'
													else: return 'True'
												elif obj[18]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[16]<=2.0:
												# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.9799, "depth": 12}
												if obj[17]<=2.0:
													# {"feature": "Children", "instances": 18, "metric_value": 0.8524, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 14}
														if obj[14]>0.0:
															return 'False'
														elif obj[14]<=0.0:
															# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[3]<=30:
																return 'False'
															elif obj[3]>30:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[10]>0:
														# {"feature": "Maritalstatus", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[9]<=0:
															# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[2]>0:
																# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[18]>0.0:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=30:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=1:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=0.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[18]<=0.0:
																	return 'False'
																else: return 'False'
															elif obj[2]<=0:
																return 'False'
															else: return 'False'
														elif obj[9]>0:
															# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]>55:
																	return 'True'
																elif obj[3]<=55:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[17]>2.0:
													# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[10]<=0:
														return 'True'
													elif obj[10]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[13]>4:
											# {"feature": "Children", "instances": 12, "metric_value": 0.65, "depth": 11}
											if obj[10]<=0:
												return 'True'
											elif obj[10]>0:
												# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[2]>0:
													# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9]<=0:
														# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[18]<=1.0:
															return 'True'
														elif obj[18]>1.0:
															return 'False'
														else: return 'False'
													elif obj[9]>0:
														return 'False'
													else: return 'False'
												elif obj[2]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=1:
										# {"feature": "Carryaway", "instances": 37, "metric_value": 0.7532, "depth": 10}
										if obj[16]>1.0:
											# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.7107, "depth": 11}
											if obj[17]>2.0:
												# {"feature": "Temperature", "instances": 20, "metric_value": 0.8813, "depth": 12}
												if obj[3]<=30:
													# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.4395, "depth": 13}
													if obj[9]<=1:
														return 'True'
													elif obj[9]>1:
														# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[14]>0.0:
															return 'True'
														elif obj[14]<=0.0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[3]>30:
													# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[9]<=0:
														# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[13]>0:
															return 'True'
														elif obj[13]<=0:
															# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[19]<=0:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=1.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[19]>0:
																return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[9]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[17]<=2.0:
												# {"feature": "Bar", "instances": 16, "metric_value": 0.3373, "depth": 12}
												if obj[14]<=1.0:
													return 'True'
												elif obj[14]>1.0:
													# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2]<=0:
														return 'True'
													elif obj[2]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[16]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[11]>4:
									return 'False'
								else: return 'False'
							elif obj[12]>6.994535519125683:
								# {"feature": "Income", "instances": 83, "metric_value": 0.9999, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Restaurant20to50", "instances": 52, "metric_value": 0.9829, "depth": 9}
									if obj[18]<=2.0:
										# {"feature": "Education", "instances": 49, "metric_value": 0.9633, "depth": 10}
										if obj[11]>0:
											# {"feature": "Age", "instances": 33, "metric_value": 0.885, "depth": 11}
											if obj[8]<=2:
												# {"feature": "Restaurantlessthan20", "instances": 22, "metric_value": 0.976, "depth": 12}
												if obj[17]>1.0:
													# {"feature": "Carryaway", "instances": 18, "metric_value": 1.0, "depth": 13}
													if obj[16]<=3.0:
														# {"feature": "Bar", "instances": 16, "metric_value": 0.9887, "depth": 14}
														if obj[14]<=2.0:
															# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 15}
															if obj[3]<=55:
																# {"feature": "Maritalstatus", "instances": 8, "metric_value": 1.0, "depth": 16}
																if obj[9]>0:
																	# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[2]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'True'
																		elif obj[10]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[9]<=0:
																	return 'False'
																else: return 'False'
															elif obj[3]>55:
																return 'True'
															else: return 'True'
														elif obj[14]>2.0:
															# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[3]>30:
																return 'False'
															elif obj[3]<=30:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	return 'True'
																elif obj[2]>0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														else: return 'False'
													elif obj[16]>3.0:
														return 'True'
													else: return 'True'
												elif obj[17]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[8]>2:
												# {"feature": "Children", "instances": 11, "metric_value": 0.4395, "depth": 12}
												if obj[10]<=0:
													return 'False'
												elif obj[10]>0:
													# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=80:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=1:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=3.0:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=3.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[7]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=0:
											# {"feature": "Age", "instances": 16, "metric_value": 0.9887, "depth": 11}
											if obj[8]>2:
												# {"feature": "Carryaway", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[16]>1.0:
													# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[9]<=1:
														# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[17]>1.0:
															return 'True'
														elif obj[17]<=1.0:
															# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[14]<=1.0:
																return 'False'
															elif obj[14]>1.0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[9]>1:
														return 'False'
													else: return 'False'
												elif obj[16]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[8]<=2:
												# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[3]<=30:
													return 'False'
												elif obj[3]>30:
													# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[9]>0:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=1.0:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=1.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[9]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[18]>2.0:
										return 'True'
									else: return 'True'
								elif obj[13]>4:
									# {"feature": "Age", "instances": 31, "metric_value": 0.9383, "depth": 9}
									if obj[8]<=6:
										# {"feature": "Temperature", "instances": 28, "metric_value": 0.8631, "depth": 10}
										if obj[3]<=30:
											# {"feature": "Carryaway", "instances": 14, "metric_value": 0.9852, "depth": 11}
											if obj[16]<=3.0:
												# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=3:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[7]>0:
														# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[10]>0:
															# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[18]<=2.0:
																return 'True'
															elif obj[18]>2.0:
																return 'False'
															else: return 'False'
														elif obj[10]<=0:
															return 'False'
														else: return 'False'
													elif obj[7]<=0:
														return 'True'
													else: return 'True'
												elif obj[11]>3:
													return 'False'
												else: return 'False'
											elif obj[16]>3.0:
												return 'False'
											else: return 'False'
										elif obj[3]>30:
											# {"feature": "Carryaway", "instances": 14, "metric_value": 0.5917, "depth": 11}
											if obj[16]<=2.0:
												return 'True'
											elif obj[16]>2.0:
												# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[9]>0:
													# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[11]<=2:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=2.0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[11]>2:
														return 'True'
													else: return 'True'
												elif obj[9]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[8]>6:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[4]>1:
							# {"feature": "Age", "instances": 24, "metric_value": 0.5436, "depth": 7}
							if obj[8]>0:
								# {"feature": "Carryaway", "instances": 22, "metric_value": 0.2668, "depth": 8}
								if obj[16]<=3.0:
									return 'True'
								elif obj[16]>3.0:
									# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[15]<=0.0:
				# {"feature": "Education", "instances": 472, "metric_value": 0.9605, "depth": 4}
				if obj[11]<=3:
					# {"feature": "Driving_to", "instances": 429, "metric_value": 0.9766, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Occupation", "instances": 335, "metric_value": 0.9437, "depth": 6}
						if obj[12]>0:
							# {"feature": "Income", "instances": 320, "metric_value": 0.9544, "depth": 7}
							if obj[13]>3:
								# {"feature": "Bar", "instances": 211, "metric_value": 0.9068, "depth": 8}
								if obj[14]<=0.0:
									# {"feature": "Temperature", "instances": 135, "metric_value": 0.9665, "depth": 9}
									if obj[3]>30:
										# {"feature": "Time", "instances": 114, "metric_value": 0.9857, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Carryaway", "instances": 98, "metric_value": 0.9563, "depth": 11}
											if obj[16]<=2.0:
												# {"feature": "Passanger", "instances": 81, "metric_value": 0.9867, "depth": 12}
												if obj[1]>0:
													# {"feature": "Age", "instances": 77, "metric_value": 0.994, "depth": 13}
													if obj[8]>1:
														# {"feature": "Restaurantlessthan20", "instances": 54, "metric_value": 0.951, "depth": 14}
														if obj[17]>0.0:
															# {"feature": "Direction_same", "instances": 48, "metric_value": 0.9799, "depth": 15}
															if obj[19]<=0:
																# {"feature": "Distance", "instances": 40, "metric_value": 0.9982, "depth": 16}
																if obj[20]<=2:
																	# {"feature": "Weather", "instances": 35, "metric_value": 0.9994, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Gender", "instances": 34, "metric_value": 0.9975, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.9641, "depth": 19}
																			if obj[9]<=2:
																				# {"feature": "Children", "instances": 17, "metric_value": 0.9367, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 21}
																					if obj[18]>0.0:
																						return 'False'
																					elif obj[18]<=0.0:
																						return 'False'
																					else: return 'False'
																				elif obj[10]<=0:
																					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[18]>0.0:
																						return 'False'
																					elif obj[18]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[9]>2:
																				return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.9887, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Children", "instances": 15, "metric_value": 0.971, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=0.0:
																						return 'False'
																					elif obj[18]>0.0:
																						return 'False'
																					else: return 'False'
																				elif obj[10]<=0:
																					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 21}
																					if obj[18]>0.0:
																						return 'True'
																					elif obj[18]<=0.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[9]>1:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[2]>0:
																		return 'True'
																	else: return 'True'
																elif obj[20]>2:
																	# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[18]<=0.0:
																		return 'True'
																	elif obj[18]>0.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[19]>0:
																# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 16}
																if obj[9]<=1:
																	return 'True'
																elif obj[9]>1:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]>0:
																		return 'False'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'True'
														elif obj[17]<=0.0:
															return 'True'
														else: return 'True'
													elif obj[8]<=1:
														# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.9321, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Restaurantlessthan20", "instances": 22, "metric_value": 0.9024, "depth": 15}
															if obj[17]>-1.0:
																# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9183, "depth": 16}
																if obj[18]<=1.0:
																	# {"feature": "Children", "instances": 14, "metric_value": 0.8631, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Gender", "instances": 12, "metric_value": 0.9183, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 19}
																			if obj[20]<=1:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[20]>1:
																				return 'False'
																			else: return 'False'
																		elif obj[7]<=0:
																			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[20]>2:
																						return 'True'
																					elif obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[10]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[18]>1.0:
																	# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[19]<=0:
																			# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[20]>1:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[20]<=1:
																				return 'False'
																			else: return 'False'
																		elif obj[19]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[19]<=0:
																			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[19]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[17]<=-1.0:
																return 'False'
															else: return 'False'
														elif obj[9]>1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											elif obj[16]>2.0:
												# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.5226, "depth": 12}
												if obj[18]<=2.0:
													# {"feature": "Children", "instances": 16, "metric_value": 0.3373, "depth": 13}
													if obj[10]>0:
														return 'True'
													elif obj[10]<=0:
														# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[7]<=0:
															return 'True'
														elif obj[7]>0:
															# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[1]<=1:
																# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[20]<=2:
																	return 'False'
																elif obj[20]>2:
																	return 'True'
																else: return 'True'
															elif obj[1]>1:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[18]>2.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[4]>3:
											# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 11}
											if obj[18]>0.0:
												return 'False'
											elif obj[18]<=0.0:
												# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8]>0:
														# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[10]>0:
															return 'False'
														elif obj[10]<=0:
															return 'True'
														else: return 'True'
													elif obj[8]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]<=30:
										# {"feature": "Time", "instances": 21, "metric_value": 0.7025, "depth": 10}
										if obj[4]>2:
											return 'True'
										elif obj[4]<=2:
											# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 11}
											if obj[2]>0:
												# {"feature": "Carryaway", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[16]<=2.0:
													# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[8]>0:
														# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[1]>1:
															# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]>0:
																return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														elif obj[1]<=1:
															return 'False'
														else: return 'False'
													elif obj[8]<=0:
														return 'True'
													else: return 'True'
												elif obj[16]>2.0:
													return 'True'
												else: return 'True'
											elif obj[2]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[14]>0.0:
									# {"feature": "Time", "instances": 76, "metric_value": 0.7166, "depth": 9}
									if obj[4]<=3:
										# {"feature": "Restaurantlessthan20", "instances": 61, "metric_value": 0.5606, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Age", "instances": 39, "metric_value": 0.2918, "depth": 11}
											if obj[8]>1:
												return 'True'
											elif obj[8]<=1:
												# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 12}
												if obj[20]<=1:
													# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[9]>0:
														# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[2]<=1:
															return 'True'
														elif obj[2]>1:
															# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[1]<=1:
																return 'False'
															elif obj[1]>1:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[9]<=0:
														return 'False'
													else: return 'False'
												elif obj[20]>1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[17]<=1.0:
											# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.8454, "depth": 11}
											if obj[9]>0:
												# {"feature": "Weather", "instances": 16, "metric_value": 0.9544, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 13}
													if obj[1]<=1:
														# {"feature": "Temperature", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[3]>55:
															# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 15}
															if obj[8]<=4:
																return 'True'
															elif obj[8]>4:
																# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[19]<=0:
																	return 'True'
																elif obj[19]>0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[3]<=55:
															return 'False'
														else: return 'False'
													elif obj[1]>1:
														return 'False'
													else: return 'False'
												elif obj[2]>0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>3:
										# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Temperature", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[3]>30:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[7]<=0:
													return 'False'
												elif obj[7]>0:
													# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=4:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[20]>1:
															return 'False'
														elif obj[20]<=1:
															return 'True'
														else: return 'True'
													elif obj[8]>4:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=30:
												# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[2]<=0:
													return 'True'
												elif obj[2]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[13]<=3:
								# {"feature": "Carryaway", "instances": 109, "metric_value": 0.9985, "depth": 8}
								if obj[16]>0.0:
									# {"feature": "Time", "instances": 102, "metric_value": 0.9997, "depth": 9}
									if obj[4]>0:
										# {"feature": "Age", "instances": 92, "metric_value": 0.9945, "depth": 10}
										if obj[8]<=4:
											# {"feature": "Restaurant20to50", "instances": 71, "metric_value": 0.9987, "depth": 11}
											if obj[18]>0.0:
												# {"feature": "Passanger", "instances": 43, "metric_value": 0.933, "depth": 12}
												if obj[1]<=2:
													# {"feature": "Bar", "instances": 25, "metric_value": 0.7219, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.3228, "depth": 14}
														if obj[17]<=2.0:
															return 'True'
														elif obj[17]>2.0:
															# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[9]>0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=55:
																	return 'False'
																elif obj[3]>55:
																	return 'True'
																else: return 'True'
															elif obj[9]<=0:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[14]>1.0:
														# {"feature": "Maritalstatus", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[3]>30:
																return 'False'
															elif obj[3]<=30:
																# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[2]>0:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[2]<=0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[9]>1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[1]>2:
													# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 13}
													if obj[20]>1:
														# {"feature": "Temperature", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[14]<=2.0:
																return 'True'
															elif obj[14]>2.0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	return 'False'
																elif obj[2]>0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[3]>55:
															# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[7]>0:
																return 'False'
															elif obj[7]<=0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=1:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=1.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[20]<=1:
														# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[14]<=1.0:
															return 'False'
														elif obj[14]>1.0:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'False'
											elif obj[18]<=0.0:
												# {"feature": "Restaurantlessthan20", "instances": 28, "metric_value": 0.9059, "depth": 12}
												if obj[17]<=3.0:
													# {"feature": "Children", "instances": 27, "metric_value": 0.8767, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 14}
														if obj[14]<=1.0:
															return 'False'
														elif obj[14]>1.0:
															# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[1]<=1:
																# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[3]>30:
																	return 'False'
																elif obj[3]<=30:
																	return 'True'
																else: return 'True'
															elif obj[1]>1:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[10]>0:
														# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 14}
														if obj[20]<=2:
															# {"feature": "Weather", "instances": 11, "metric_value": 0.9457, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 16}
																if obj[1]<=2:
																	# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[19]<=0:
																			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[3]<=55:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		elif obj[19]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[9]>0:
																		return 'True'
																	else: return 'True'
																elif obj[1]>2:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														elif obj[20]>2:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[17]>3.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[8]>4:
											# {"feature": "Restaurantlessthan20", "instances": 21, "metric_value": 0.7919, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.896, "depth": 12}
												if obj[19]<=0:
													# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 13}
													if obj[14]>0.0:
														# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[2]<=1:
															# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 15}
															if obj[1]<=2:
																# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[10]>0:
																		return 'False'
																	elif obj[10]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	return 'True'
																else: return 'True'
															elif obj[1]>2:
																return 'False'
															else: return 'False'
														elif obj[2]>1:
															return 'True'
														else: return 'True'
													elif obj[14]<=0.0:
														# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[20]<=2:
															return 'False'
														elif obj[20]>2:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=55:
																return 'False'
															elif obj[3]>55:
																return 'True'
															else: return 'True'
														else: return 'False'
													else: return 'False'
												elif obj[19]>0:
													return 'False'
												else: return 'False'
											elif obj[17]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[4]<=0:
										# {"feature": "Temperature", "instances": 10, "metric_value": 0.7219, "depth": 10}
										if obj[3]<=55:
											# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[8]>1:
												# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[2]<=0:
													return 'False'
												elif obj[2]>0:
													return 'True'
												else: return 'True'
											elif obj[8]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]>55:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[16]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[12]<=0:
							# {"feature": "Income", "instances": 15, "metric_value": 0.3534, "depth": 7}
							if obj[13]>0:
								return 'True'
							elif obj[13]<=0:
								# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=55:
									return 'True'
								elif obj[3]>55:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 94, "metric_value": 0.979, "depth": 6}
						if obj[4]<=0:
							# {"feature": "Occupation", "instances": 69, "metric_value": 0.9031, "depth": 7}
							if obj[12]<=6:
								# {"feature": "Income", "instances": 41, "metric_value": 0.6594, "depth": 8}
								if obj[13]>1:
									# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.7706, "depth": 9}
									if obj[18]<=1.0:
										# {"feature": "Bar", "instances": 24, "metric_value": 0.8709, "depth": 10}
										if obj[14]<=1.0:
											# {"feature": "Carryaway", "instances": 21, "metric_value": 0.9183, "depth": 11}
											if obj[16]>1.0:
												# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.9641, "depth": 12}
												if obj[17]<=2.0:
													# {"feature": "Passanger", "instances": 12, "metric_value": 1.0, "depth": 13}
													if obj[1]>0:
														# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[9]>0:
															# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[2]<=0:
																return 'False'
															elif obj[2]>0:
																# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[8]>3:
																	return 'False'
																elif obj[8]<=3:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[9]<=0:
															# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[3]>30:
																# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[8]<=1:
																		# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[19]<=0:
																			return 'False'
																		elif obj[19]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[8]>1:
																		return 'False'
																	else: return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															elif obj[3]<=30:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[1]<=0:
														return 'True'
													else: return 'True'
												elif obj[17]>2.0:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]>0:
															return 'True'
														elif obj[1]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'False'
											elif obj[16]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[14]>1.0:
											return 'False'
										else: return 'False'
									elif obj[18]>1.0:
										return 'False'
									else: return 'False'
								elif obj[13]<=1:
									return 'False'
								else: return 'False'
							elif obj[12]>6:
								# {"feature": "Carryaway", "instances": 28, "metric_value": 0.9963, "depth": 8}
								if obj[16]>1.0:
									# {"feature": "Weather", "instances": 19, "metric_value": 0.8997, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.7871, "depth": 10}
										if obj[9]>0:
											# {"feature": "Temperature", "instances": 13, "metric_value": 0.8905, "depth": 11}
											if obj[3]>30:
												# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[7]<=0:
													# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1]>0:
														return 'True'
													elif obj[1]<=0:
														# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[14]<=1.0:
															return 'True'
														elif obj[14]>1.0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[7]>0:
													# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8]<=1:
														# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[13]>2:
															# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[19]<=0:
																return 'False'
															elif obj[19]>0:
																return 'True'
															else: return 'True'
														elif obj[13]<=2:
															return 'True'
														else: return 'True'
													elif obj[8]>1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[9]<=0:
											return 'True'
										else: return 'True'
									elif obj[2]>1:
										return 'False'
									else: return 'False'
								elif obj[16]<=1.0:
									# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[8]<=4:
										return 'False'
									elif obj[8]>4:
										# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[13]<=6:
											return 'True'
										elif obj[13]>6:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[4]>0:
							# {"feature": "Age", "instances": 25, "metric_value": 0.9044, "depth": 7}
							if obj[8]<=6:
								# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.8281, "depth": 8}
								if obj[9]>0:
									# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 9}
									if obj[12]>3:
										# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[13]>1:
											# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.994, "depth": 11}
											if obj[17]<=2.0:
												# {"feature": "Weather", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Carryaway", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[16]<=2.0:
														return 'False'
													elif obj[16]>2.0:
														# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]<=55:
															return 'False'
														elif obj[3]>55:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[2]>0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7]<=0:
														return 'True'
													elif obj[7]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[17]>2.0:
												return 'True'
											else: return 'True'
										elif obj[13]<=1:
											return 'True'
										else: return 'True'
									elif obj[12]<=3:
										return 'True'
									else: return 'True'
								elif obj[9]<=0:
									return 'True'
								else: return 'True'
							elif obj[8]>6:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[11]>3:
					# {"feature": "Children", "instances": 43, "metric_value": 0.5186, "depth": 5}
					if obj[10]<=0:
						return 'True'
					elif obj[10]>0:
						# {"feature": "Direction_same", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[19]<=0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[4]>0:
								# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[8]<=2:
										# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[0]<=0:
											# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[2]>1:
												return 'True'
											elif obj[2]<=1:
												return 'False'
											else: return 'False'
										elif obj[0]>0:
											return 'False'
										else: return 'False'
									elif obj[8]>2:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						elif obj[19]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>0:
			# {"feature": "Driving_to", "instances": 1839, "metric_value": 0.9963, "depth": 3}
			if obj[0]<=0:
				# {"feature": "Coffeehouse", "instances": 995, "metric_value": 0.9573, "depth": 4}
				if obj[15]>0.0:
					# {"feature": "Restaurantlessthan20", "instances": 759, "metric_value": 0.9222, "depth": 5}
					if obj[17]>0.0:
						# {"feature": "Distance", "instances": 748, "metric_value": 0.927, "depth": 6}
						if obj[20]>1:
							# {"feature": "Temperature", "instances": 395, "metric_value": 0.9579, "depth": 7}
							if obj[3]>55:
								# {"feature": "Time", "instances": 325, "metric_value": 0.932, "depth": 8}
								if obj[4]>0:
									# {"feature": "Age", "instances": 259, "metric_value": 0.9672, "depth": 9}
									if obj[8]<=6:
										# {"feature": "Maritalstatus", "instances": 242, "metric_value": 0.9782, "depth": 10}
										if obj[9]<=2:
											# {"feature": "Income", "instances": 230, "metric_value": 0.9684, "depth": 11}
											if obj[13]>0:
												# {"feature": "Restaurant20to50", "instances": 200, "metric_value": 0.9507, "depth": 12}
												if obj[18]<=2.0:
													# {"feature": "Occupation", "instances": 187, "metric_value": 0.965, "depth": 13}
													if obj[12]<=14:
														# {"feature": "Carryaway", "instances": 175, "metric_value": 0.956, "depth": 14}
														if obj[16]>2.0:
															# {"feature": "Bar", "instances": 90, "metric_value": 0.9825, "depth": 15}
															if obj[14]>0.0:
																# {"feature": "Passanger", "instances": 58, "metric_value": 0.9444, "depth": 16}
																if obj[1]>0:
																	# {"feature": "Gender", "instances": 56, "metric_value": 0.9544, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Education", "instances": 30, "metric_value": 0.8813, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Children", "instances": 23, "metric_value": 0.7554, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 16, "metric_value": 0.8113, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[11]>2:
																			# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		# {"feature": "Education", "instances": 26, "metric_value": 0.9957, "depth": 18}
																		if obj[11]<=3:
																			# {"feature": "Children", "instances": 23, "metric_value": 0.9986, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 14, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 9, "metric_value": 0.9911, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[11]>3:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[1]<=0:
																	return 'True'
																else: return 'True'
															elif obj[14]<=0.0:
																# {"feature": "Passanger", "instances": 32, "metric_value": 0.9972, "depth": 16}
																if obj[1]>2:
																	# {"feature": "Children", "instances": 19, "metric_value": 0.9495, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 18}
																		if obj[11]<=0:
																			# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		elif obj[11]>0:
																			# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[10]<=0:
																		# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[11]<=0:
																				return 'True'
																			elif obj[11]>0:
																				return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[11]<=1:
																				return 'False'
																			elif obj[11]>1:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	else: return 'False'
																elif obj[1]<=2:
																	# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 17}
																	if obj[11]<=1:
																		# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[10]>0:
																				return 'True'
																			elif obj[10]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[11]>1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			return 'True'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[16]<=2.0:
															# {"feature": "Education", "instances": 85, "metric_value": 0.9143, "depth": 15}
															if obj[11]<=3:
																# {"feature": "Bar", "instances": 80, "metric_value": 0.896, "depth": 16}
																if obj[14]<=3.0:
																	# {"feature": "Passanger", "instances": 77, "metric_value": 0.8797, "depth": 17}
																	if obj[1]>0:
																		# {"feature": "Gender", "instances": 71, "metric_value": 0.893, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Children", "instances": 43, "metric_value": 0.9103, "depth": 19}
																			if obj[10]>0:
																				# {"feature": "Weather", "instances": 28, "metric_value": 0.9403, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 28, "metric_value": 0.9403, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]<=0:
																				# {"feature": "Weather", "instances": 15, "metric_value": 0.8366, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 15, "metric_value": 0.8366, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Children", "instances": 28, "metric_value": 0.8631, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 18, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 10, "metric_value": 0.7219, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[1]<=0:
																		# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[14]>3.0:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=3:
																			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[11]>3:
																# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[14]>0.0:
																	return 'False'
																elif obj[14]<=0.0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													elif obj[12]>14:
														# {"feature": "Carryaway", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[16]<=2.0:
															# {"feature": "Passanger", "instances": 10, "metric_value": 0.8813, "depth": 15}
															if obj[1]>0:
																# {"feature": "Children", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[10]<=0:
																	return 'False'
																elif obj[10]>0:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]<=0:
																		return 'False'
																	elif obj[7]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[1]<=0:
																# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14]<=2.0:
																	return 'True'
																elif obj[14]>2.0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[16]>2.0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[18]>2.0:
													# {"feature": "Education", "instances": 13, "metric_value": 0.3912, "depth": 13}
													if obj[11]>0:
														return 'True'
													elif obj[11]<=0:
														# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[7]>0:
															return 'True'
														elif obj[7]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											elif obj[13]<=0:
												# {"feature": "Occupation", "instances": 30, "metric_value": 0.9871, "depth": 12}
												if obj[12]<=9:
													# {"feature": "Passanger", "instances": 24, "metric_value": 0.995, "depth": 13}
													if obj[1]>1:
														# {"feature": "Bar", "instances": 20, "metric_value": 0.9928, "depth": 14}
														if obj[14]>0.0:
															# {"feature": "Gender", "instances": 18, "metric_value": 0.9641, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 16}
																if obj[11]>0:
																	# {"feature": "Carryaway", "instances": 11, "metric_value": 0.9457, "depth": 17}
																	if obj[16]>2.0:
																		# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[18]>1.0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[18]<=1.0:
																				return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[16]<=2.0:
																		return 'True'
																	else: return 'True'
																elif obj[11]<=0:
																	return 'False'
																else: return 'False'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[14]<=0.0:
															return 'True'
														else: return 'True'
													elif obj[1]<=1:
														return 'True'
													else: return 'True'
												elif obj[12]>9:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>2:
											# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 11}
											if obj[18]>1.0:
												# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[1]>2:
													# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[12]>7:
														return 'True'
													elif obj[12]<=7:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=1:
																# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10]<=1:
																	# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[11]<=3:
																		# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[13]<=3:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=0.0:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=4.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[1]<=2:
													return 'False'
												else: return 'False'
											elif obj[18]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>6:
										# {"feature": "Maritalstatus", "instances": 17, "metric_value": 0.5226, "depth": 10}
										if obj[9]<=0:
											return 'True'
										elif obj[9]>0:
											# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[1]>2:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7]<=0:
													return 'True'
												elif obj[7]>0:
													# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2]<=0:
														# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11]<=2:
																# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12]<=2:
																	# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13]<=2:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=0.0:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=1.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=0.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[1]<=2:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Education", "instances": 66, "metric_value": 0.65, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Bar", "instances": 51, "metric_value": 0.7522, "depth": 10}
										if obj[14]<=2.0:
											# {"feature": "Restaurant20to50", "instances": 46, "metric_value": 0.6666, "depth": 11}
											if obj[18]<=1.0:
												# {"feature": "Carryaway", "instances": 28, "metric_value": 0.8113, "depth": 12}
												if obj[16]>1.0:
													# {"feature": "Age", "instances": 24, "metric_value": 0.8709, "depth": 13}
													if obj[8]>0:
														# {"feature": "Occupation", "instances": 21, "metric_value": 0.9183, "depth": 14}
														if obj[12]<=16:
															# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 15}
															if obj[13]>0:
																# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.9183, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Children", "instances": 15, "metric_value": 0.8366, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[1]<=3:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[1]<=3:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[10]>0:
																		# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[1]<=3:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[9]>1:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]<=0:
																		return 'False'
																	elif obj[7]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[13]<=0:
																return 'False'
															else: return 'False'
														elif obj[12]>16:
															return 'True'
														else: return 'True'
													elif obj[8]<=0:
														return 'True'
													else: return 'True'
												elif obj[16]<=1.0:
													return 'True'
												else: return 'True'
											elif obj[18]>1.0:
												# {"feature": "Income", "instances": 18, "metric_value": 0.3095, "depth": 12}
												if obj[13]>0:
													return 'True'
												elif obj[13]<=0:
													# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8]>1:
														return 'True'
													elif obj[8]<=1:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[14]>2.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[7]>0:
												# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8]<=1:
													return 'True'
												elif obj[8]>1:
													return 'False'
												else: return 'False'
											elif obj[7]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[11]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=55:
								# {"feature": "Education", "instances": 70, "metric_value": 0.9976, "depth": 8}
								if obj[11]>1:
									# {"feature": "Maritalstatus", "instances": 37, "metric_value": 0.974, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Age", "instances": 31, "metric_value": 0.9992, "depth": 10}
										if obj[8]<=2:
											# {"feature": "Income", "instances": 18, "metric_value": 0.8524, "depth": 11}
											if obj[13]>3:
												# {"feature": "Gender", "instances": 11, "metric_value": 0.994, "depth": 12}
												if obj[7]<=0:
													# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[12]>4:
														# {"feature": "Carryaway", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[16]<=2.0:
															# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[2]<=1:
																return 'False'
															elif obj[2]>1:
																return 'True'
															else: return 'True'
														elif obj[16]>2.0:
															return 'True'
														else: return 'True'
													elif obj[12]<=4:
														return 'True'
													else: return 'True'
												elif obj[7]>0:
													return 'False'
												else: return 'False'
											elif obj[13]<=3:
												return 'True'
											else: return 'True'
										elif obj[8]>2:
											# {"feature": "Occupation", "instances": 13, "metric_value": 0.7793, "depth": 11}
											if obj[12]>8:
												# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[18]>0.0:
														# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[14]>0.0:
															return 'False'
														elif obj[14]<=0.0:
															# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[1]<=2:
																# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[4]<=0:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=1:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[13]<=0:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[18]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[2]>0:
													return 'True'
												else: return 'True'
											elif obj[12]<=8:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								elif obj[11]<=1:
									# {"feature": "Carryaway", "instances": 33, "metric_value": 0.9183, "depth": 9}
									if obj[16]>2.0:
										# {"feature": "Children", "instances": 17, "metric_value": 0.5226, "depth": 10}
										if obj[10]>0:
											return 'False'
										elif obj[10]<=0:
											# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[8]<=6:
												# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[2]<=1:
													return 'False'
												elif obj[2]>1:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=0:
														# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[4]<=2:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=1:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[12]<=6:
																		# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[13]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=1.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>6:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[16]<=2.0:
										# {"feature": "Time", "instances": 16, "metric_value": 0.9887, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[8]>1:
												# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[12]>1:
													# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[13]<=4:
														return 'False'
													elif obj[13]>4:
														return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											elif obj[8]<=1:
												return 'False'
											else: return 'False'
										elif obj[4]>0:
											# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[8]<=4:
												return 'True'
											elif obj[8]>4:
												# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1]<=0:
													return 'False'
												elif obj[1]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[20]<=1:
							# {"feature": "Carryaway", "instances": 353, "metric_value": 0.8816, "depth": 7}
							if obj[16]<=3.0:
								# {"feature": "Income", "instances": 297, "metric_value": 0.8454, "depth": 8}
								if obj[13]<=6:
									# {"feature": "Time", "instances": 246, "metric_value": 0.8015, "depth": 9}
									if obj[4]>2:
										# {"feature": "Restaurant20to50", "instances": 141, "metric_value": 0.7046, "depth": 10}
										if obj[18]>0.0:
											# {"feature": "Maritalstatus", "instances": 117, "metric_value": 0.64, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Age", "instances": 96, "metric_value": 0.5436, "depth": 12}
												if obj[8]>0:
													# {"feature": "Bar", "instances": 78, "metric_value": 0.3912, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Temperature", "instances": 56, "metric_value": 0.4912, "depth": 14}
														if obj[3]>55:
															# {"feature": "Children", "instances": 32, "metric_value": 0.6253, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 16}
																if obj[1]>0:
																	# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 17}
																	if obj[12]>1:
																		# {"feature": "Gender", "instances": 12, "metric_value": 0.9183, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 19}
																			if obj[11]>0:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[11]<=0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[11]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'False'
																		else: return 'False'
																	elif obj[12]<=1:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=0:
																	return 'True'
																else: return 'True'
															elif obj[10]>0:
																# {"feature": "Passanger", "instances": 16, "metric_value": 0.3373, "depth": 16}
																if obj[1]>1:
																	return 'True'
																elif obj[1]<=1:
																	# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[11]<=1:
																		return 'True'
																	elif obj[11]>1:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=1:
																				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[12]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'True'
															else: return 'True'
														elif obj[3]<=55:
															# {"feature": "Occupation", "instances": 24, "metric_value": 0.2499, "depth": 15}
															if obj[12]<=7:
																return 'True'
															elif obj[12]>7:
																# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[7]>0:
																	return 'True'
																elif obj[7]<=0:
																	# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[1]>0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]>0:
																			return 'False'
																		elif obj[11]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[1]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[14]>1.0:
														return 'True'
													else: return 'True'
												elif obj[8]<=0:
													# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 13}
													if obj[14]<=2.0:
														# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 14}
														if obj[11]>1:
															return 'True'
														elif obj[11]<=1:
															# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 15}
															if obj[1]>2:
																# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[3]<=30:
																	return 'True'
																elif obj[3]>30:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]>0:
																		return 'True'
																	elif obj[10]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[1]<=2:
																return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[14]>2.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[9]>1:
												# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 12}
												if obj[11]>0:
													# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 13}
													if obj[12]<=16:
														# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[7]>0:
																# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[3]>55:
																	# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[8]>0:
																		return 'False'
																	elif obj[8]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[3]<=55:
																	return 'True'
																else: return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														elif obj[1]>1:
															# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[3]>30:
																return 'True'
															elif obj[3]<=30:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]<=0:
																	return 'True'
																elif obj[7]>0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														else: return 'True'
													elif obj[12]>16:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[12]<=5:
														return 'True'
													elif obj[12]>5:
														# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1]>0:
															return 'True'
														elif obj[1]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[18]<=0.0:
											# {"feature": "Maritalstatus", "instances": 24, "metric_value": 0.9183, "depth": 11}
											if obj[9]>0:
												# {"feature": "Bar", "instances": 14, "metric_value": 0.5917, "depth": 12}
												if obj[14]>0.0:
													# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 13}
													if obj[3]>30:
														# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[11]<=3:
															# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[1]>0:
																# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[8]<=1:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[12]<=5:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[8]<=3:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[12]<=10:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[1]<=0:
																return 'True'
															else: return 'True'
														elif obj[11]>3:
															return 'True'
														else: return 'True'
													elif obj[3]<=30:
														return 'True'
													else: return 'True'
												elif obj[14]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[9]<=0:
												# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[8]>1:
													# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 13}
													if obj[1]>1:
														# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[11]<=0:
															return 'False'
														elif obj[11]>0:
															# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[12]<=9:
																return 'True'
															elif obj[12]>9:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[1]<=1:
														return 'True'
													else: return 'True'
												elif obj[8]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[4]<=2:
										# {"feature": "Education", "instances": 105, "metric_value": 0.8981, "depth": 10}
										if obj[11]>1:
											# {"feature": "Age", "instances": 58, "metric_value": 0.9923, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Occupation", "instances": 49, "metric_value": 0.9997, "depth": 12}
												if obj[12]<=11:
													# {"feature": "Restaurant20to50", "instances": 35, "metric_value": 0.971, "depth": 13}
													if obj[18]<=2.0:
														# {"feature": "Maritalstatus", "instances": 32, "metric_value": 0.9284, "depth": 14}
														if obj[9]<=2:
															# {"feature": "Weather", "instances": 30, "metric_value": 0.9481, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 25, "metric_value": 0.9044, "depth": 16}
																if obj[3]>55:
																	# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 17}
																	if obj[14]<=1.0:
																		# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 19}
																			if obj[1]>0:
																				# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[10]<=0:
																					return 'False'
																				else: return 'False'
																			elif obj[1]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[14]>1.0:
																		# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[1]>0:
																			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		elif obj[1]<=0:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[3]<=55:
																	# {"feature": "Bar", "instances": 11, "metric_value": 0.684, "depth": 17}
																	if obj[14]<=1.0:
																		return 'False'
																	elif obj[14]>1.0:
																		# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					return 'True'
																				elif obj[10]>0:
																					return 'False'
																				else: return 'False'
																			elif obj[1]>1:
																				return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																else: return 'False'
															elif obj[2]>0:
																# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[14]>0.0:
																	# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[1]>1:
																		return 'True'
																	else: return 'True'
																elif obj[14]<=0.0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[9]>2:
															return 'False'
														else: return 'False'
													elif obj[18]>2.0:
														return 'True'
													else: return 'True'
												elif obj[12]>11:
													# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 13}
													if obj[14]>1.0:
														# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[7]>0:
															# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[3]>55:
																return 'False'
															elif obj[3]<=55:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=1:
																	return 'False'
																elif obj[1]>1:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													elif obj[14]<=1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]>4:
												# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[12]>0:
													return 'True'
												elif obj[12]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[11]<=1:
											# {"feature": "Restaurant20to50", "instances": 47, "metric_value": 0.6072, "depth": 11}
											if obj[18]>0.0:
												# {"feature": "Temperature", "instances": 40, "metric_value": 0.469, "depth": 12}
												if obj[3]>55:
													# {"feature": "Age", "instances": 24, "metric_value": 0.2499, "depth": 13}
													if obj[8]<=3:
														return 'True'
													elif obj[8]>3:
														# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 14}
														if obj[12]<=6:
															return 'True'
														elif obj[12]>6:
															# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[14]>0.0:
																# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[1]>0:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[1]<=0:
																	return 'True'
																else: return 'True'
															elif obj[14]<=0.0:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[3]<=55:
													# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.6962, "depth": 13}
													if obj[9]<=1:
														# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[12]<=7:
															return 'True'
														elif obj[12]>7:
															# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[1]<=1:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]<=0:
																	return 'True'
																elif obj[7]>0:
																	return 'False'
																else: return 'False'
															elif obj[1]>1:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[9]>1:
														# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	return 'True'
																elif obj[7]<=0:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														elif obj[1]>1:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											elif obj[18]<=0.0:
												# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[3]<=55:
													return 'True'
												elif obj[3]>55:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[13]>6:
									# {"feature": "Occupation", "instances": 51, "metric_value": 0.9774, "depth": 9}
									if obj[12]<=19:
										# {"feature": "Bar", "instances": 48, "metric_value": 0.9544, "depth": 10}
										if obj[14]<=2.0:
											# {"feature": "Temperature", "instances": 44, "metric_value": 0.976, "depth": 11}
											if obj[3]>55:
												# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.8454, "depth": 12}
												if obj[9]<=1:
													# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 13}
													if obj[11]<=1:
														# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[8]>3:
															# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[18]>0.0:
																# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[4]<=0:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[4]>0:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=1:
																	return 'False'
																else: return 'False'
															elif obj[18]<=0.0:
																return 'True'
															else: return 'True'
														elif obj[8]<=3:
															return 'True'
														else: return 'True'
													elif obj[11]>1:
														# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[1]>0:
															# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[4]>0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[8]<=6:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[7]<=0:
																	return 'False'
																else: return 'False'
															elif obj[4]<=0:
																return 'False'
															else: return 'False'
														elif obj[1]<=0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[9]>1:
													return 'True'
												else: return 'True'
											elif obj[3]<=55:
												# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 12}
												if obj[11]<=3:
													# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.9852, "depth": 13}
													if obj[9]>0:
														# {"feature": "Time", "instances": 15, "metric_value": 0.9183, "depth": 14}
														if obj[4]>0:
															# {"feature": "Age", "instances": 14, "metric_value": 0.9403, "depth": 15}
															if obj[8]<=5:
																# {"feature": "Weather", "instances": 13, "metric_value": 0.9612, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 17}
																	if obj[18]>1.0:
																		# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[1]>1:
																			return 'False'
																		elif obj[1]<=1:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]>0:
																				return 'True'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[18]<=1.0:
																		# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[1]>1:
																			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				return 'True'
																			else: return 'True'
																		elif obj[1]<=1:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[2]>0:
																	# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=0:
																		# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[1]>0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[8]>5:
																return 'False'
															else: return 'False'
														elif obj[4]<=0:
															return 'False'
														else: return 'False'
													elif obj[9]<=0:
														# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[8]>2:
															# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=3:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[4]<=3:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[8]<=2:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[11]>3:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[14]>2.0:
											return 'True'
										else: return 'True'
									elif obj[12]>19:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[16]>3.0:
								# {"feature": "Restaurant20to50", "instances": 56, "metric_value": 0.9917, "depth": 8}
								if obj[18]<=2.0:
									# {"feature": "Bar", "instances": 48, "metric_value": 0.9544, "depth": 9}
									if obj[14]<=1.0:
										# {"feature": "Occupation", "instances": 31, "metric_value": 0.9932, "depth": 10}
										if obj[12]<=7:
											# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 11}
											if obj[11]<=2:
												# {"feature": "Temperature", "instances": 16, "metric_value": 1.0, "depth": 12}
												if obj[3]>30:
													# {"feature": "Time", "instances": 14, "metric_value": 0.9852, "depth": 13}
													if obj[4]<=2:
														# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[7]>0:
															return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													elif obj[4]>2:
														# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[7]>0:
															return 'True'
														elif obj[7]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[3]<=30:
													return 'False'
												else: return 'False'
											elif obj[11]>2:
												return 'True'
											else: return 'True'
										elif obj[12]>7:
											# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 11}
											if obj[11]>0:
												return 'False'
											elif obj[11]<=0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]>0:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=30:
														return 'False'
													elif obj[3]>30:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[14]>1.0:
										# {"feature": "Gender", "instances": 17, "metric_value": 0.3228, "depth": 10}
										if obj[7]<=0:
											return 'True'
										elif obj[7]>0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[11]>0:
												return 'True'
											elif obj[11]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[18]>2.0:
									# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[8]>0:
										return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[17]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[15]<=0.0:
					# {"feature": "Education", "instances": 236, "metric_value": 0.9995, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Income", "instances": 206, "metric_value": 0.9989, "depth": 6}
						if obj[13]<=5:
							# {"feature": "Restaurant20to50", "instances": 151, "metric_value": 0.9962, "depth": 7}
							if obj[18]<=2.0:
								# {"feature": "Bar", "instances": 147, "metric_value": 0.9984, "depth": 8}
								if obj[14]<=0.0:
									# {"feature": "Age", "instances": 82, "metric_value": 0.9961, "depth": 9}
									if obj[8]<=6:
										# {"feature": "Time", "instances": 77, "metric_value": 0.9852, "depth": 10}
										if obj[4]>2:
											# {"feature": "Restaurantlessthan20", "instances": 39, "metric_value": 0.9183, "depth": 11}
											if obj[17]>0.0:
												# {"feature": "Maritalstatus", "instances": 33, "metric_value": 0.9673, "depth": 12}
												if obj[9]<=2:
													# {"feature": "Temperature", "instances": 31, "metric_value": 0.9383, "depth": 13}
													if obj[3]>55:
														# {"feature": "Carryaway", "instances": 22, "metric_value": 0.994, "depth": 14}
														if obj[16]>-1.0:
															# {"feature": "Distance", "instances": 20, "metric_value": 1.0, "depth": 15}
															if obj[20]>1:
																# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 16}
																if obj[12]<=18:
																	# {"feature": "Children", "instances": 11, "metric_value": 0.8454, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[1]>1:
																			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[7]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[1]<=1:
																			return 'False'
																		else: return 'False'
																	elif obj[10]>0:
																		# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[1]>1:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[1]<=1:
																				return 'False'
																			else: return 'False'
																		elif obj[7]<=0:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																elif obj[12]>18:
																	return 'True'
																else: return 'True'
															elif obj[20]<=1:
																# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[10]<=0:
																	return 'True'
																elif obj[10]>0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[16]<=-1.0:
															return 'True'
														else: return 'True'
													elif obj[3]<=55:
														# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[1]>0:
															return 'True'
														elif obj[1]<=0:
															# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[16]>1.0:
																return 'True'
															elif obj[16]<=1.0:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[9]>2:
													return 'False'
												else: return 'False'
											elif obj[17]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											# {"feature": "Temperature", "instances": 38, "metric_value": 0.998, "depth": 11}
											if obj[3]>55:
												# {"feature": "Passanger", "instances": 24, "metric_value": 0.9799, "depth": 12}
												if obj[1]>2:
													# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.9984, "depth": 13}
													if obj[9]<=2:
														# {"feature": "Carryaway", "instances": 19, "metric_value": 0.998, "depth": 14}
														if obj[16]>1.0:
															# {"feature": "Gender", "instances": 16, "metric_value": 0.9887, "depth": 15}
															if obj[7]>0:
																# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 16}
																if obj[12]>1:
																	# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[20]<=1:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]>0.0:
																				return 'False'
																			elif obj[17]<=0.0:
																				return 'True'
																			else: return 'True'
																		elif obj[20]>1:
																			return 'True'
																		else: return 'True'
																	elif obj[10]>0:
																		# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=1.0:
																			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[17]>1.0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[12]<=1:
																	return 'True'
																else: return 'True'
															elif obj[7]<=0:
																# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[10]<=0:
																	return 'False'
																elif obj[10]>0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[16]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[9]>2:
														return 'True'
													else: return 'True'
												elif obj[1]<=2:
													return 'True'
												else: return 'True'
											elif obj[3]<=55:
												# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 12}
												if obj[12]<=4:
													# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[2]<=0:
														# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[7]>0:
															return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													elif obj[2]>0:
														return 'True'
													else: return 'True'
												elif obj[12]>4:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>6:
										return 'False'
									else: return 'False'
								elif obj[14]>0.0:
									# {"feature": "Distance", "instances": 65, "metric_value": 0.971, "depth": 9}
									if obj[20]>1:
										# {"feature": "Occupation", "instances": 39, "metric_value": 0.9957, "depth": 10}
										if obj[12]<=16:
											# {"feature": "Carryaway", "instances": 31, "metric_value": 0.9932, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 12}
												if obj[4]<=2:
													# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[2]<=1:
															# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[8]>4:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=3:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[9]<=2:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=4.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[8]<=4:
																return 'True'
															else: return 'True'
														elif obj[2]>1:
															return 'False'
														else: return 'False'
													elif obj[7]>0:
														# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[1]>2:
															# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[8]<=0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=3.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[8]>0:
																return 'False'
															else: return 'False'
														elif obj[1]<=2:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[4]>2:
													# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[1]>0:
														return 'True'
													elif obj[1]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]<=2.0:
												# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 12}
												if obj[8]<=1:
													# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[3]>55:
														# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[4]>2:
															# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[10]>0:
																return 'False'
															elif obj[10]<=0:
																return 'True'
															else: return 'True'
														elif obj[4]<=2:
															return 'True'
														else: return 'True'
													elif obj[3]<=55:
														return 'False'
													else: return 'False'
												elif obj[8]>1:
													# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[3]>55:
														return 'False'
													elif obj[3]<=55:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'False'
										elif obj[12]>16:
											# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[17]>1.0:
												return 'True'
											elif obj[17]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[20]<=1:
										# {"feature": "Age", "instances": 26, "metric_value": 0.7063, "depth": 10}
										if obj[8]>2:
											return 'False'
										elif obj[8]<=2:
											# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.9612, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Temperature", "instances": 10, "metric_value": 1.0, "depth": 12}
												if obj[3]>55:
													# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[1]>0:
														# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[4]>0:
															# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[12]>5:
																return 'True'
															elif obj[12]<=5:
																return 'False'
															else: return 'False'
														elif obj[4]<=0:
															return 'True'
														else: return 'True'
													elif obj[1]<=0:
														return 'False'
													else: return 'False'
												elif obj[3]<=55:
													# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]>6:
															return 'False'
														elif obj[12]<=6:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'False'
											elif obj[9]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[18]>2.0:
								return 'False'
							else: return 'False'
						elif obj[13]>5:
							# {"feature": "Occupation", "instances": 55, "metric_value": 0.9121, "depth": 7}
							if obj[12]>1:
								# {"feature": "Restaurantlessthan20", "instances": 44, "metric_value": 0.9624, "depth": 8}
								if obj[17]<=3.0:
									# {"feature": "Carryaway", "instances": 42, "metric_value": 0.9737, "depth": 9}
									if obj[16]<=2.0:
										# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.999, "depth": 10}
										if obj[18]>0.0:
											# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 11}
											if obj[1]>1:
												# {"feature": "Temperature", "instances": 11, "metric_value": 0.994, "depth": 12}
												if obj[3]>55:
													# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=2:
														# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[4]>0:
															# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[7]>0:
																# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[20]>1:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=0.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[20]<=1:
																	return 'False'
																else: return 'False'
															elif obj[7]<=0:
																return 'True'
															else: return 'True'
														elif obj[4]<=0:
															return 'False'
														else: return 'False'
													elif obj[8]>2:
														return 'False'
													else: return 'False'
												elif obj[3]<=55:
													return 'True'
												else: return 'True'
											elif obj[1]<=1:
												return 'False'
											else: return 'False'
										elif obj[18]<=0.0:
											# {"feature": "Gender", "instances": 13, "metric_value": 0.8905, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[8]>0:
													# {"feature": "Temperature", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[3]>55:
														return 'True'
													elif obj[3]<=55:
														# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[4]<=2:
																return 'False'
															elif obj[4]>2:
																return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[8]<=0:
													return 'False'
												else: return 'False'
											elif obj[7]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[16]>2.0:
										# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.8366, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 11}
											if obj[18]<=1.0:
												# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[3]>30:
													# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[20]<=1:
															return 'False'
														elif obj[20]>1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[3]<=30:
													return 'True'
												else: return 'True'
											elif obj[18]>1.0:
												return 'True'
											else: return 'True'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[17]>3.0:
									return 'True'
								else: return 'True'
							elif obj[12]<=1:
								# {"feature": "Carryaway", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[16]>1.0:
									return 'True'
								elif obj[16]<=1.0:
									# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[4]>2:
										return 'True'
									elif obj[4]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]>2:
						# {"feature": "Restaurantlessthan20", "instances": 30, "metric_value": 0.8366, "depth": 6}
						if obj[17]<=2.0:
							# {"feature": "Age", "instances": 24, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=4:
								# {"feature": "Temperature", "instances": 22, "metric_value": 0.8454, "depth": 8}
								if obj[3]>30:
									# {"feature": "Occupation", "instances": 21, "metric_value": 0.7919, "depth": 9}
									if obj[12]>5:
										# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[14]<=1.0:
											return 'False'
										elif obj[14]>1.0:
											return 'True'
										else: return 'True'
									elif obj[12]<=5:
										# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[4]>0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[1]>0:
												# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[13]>0:
													# {"feature": "Carryaway", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[16]>2.0:
														# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[7]>0:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=2.0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=1.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[7]<=0:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=0.0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=0.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[16]<=2.0:
														return 'True'
													else: return 'True'
												elif obj[13]<=0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[3]<=30:
									return 'True'
								else: return 'True'
							elif obj[8]>4:
								return 'True'
							else: return 'True'
						elif obj[17]>2.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[0]>0:
				# {"feature": "Direction_same", "instances": 844, "metric_value": 0.9877, "depth": 4}
				if obj[19]>0:
					# {"feature": "Time", "instances": 422, "metric_value": 0.9882, "depth": 5}
					if obj[4]>0:
						# {"feature": "Coffeehouse", "instances": 319, "metric_value": 0.998, "depth": 6}
						if obj[15]>0.0:
							# {"feature": "Temperature", "instances": 237, "metric_value": 0.9954, "depth": 7}
							if obj[3]>55:
								# {"feature": "Maritalstatus", "instances": 155, "metric_value": 0.9585, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Restaurantlessthan20", "instances": 147, "metric_value": 0.9374, "depth": 9}
									if obj[17]>-1.0:
										# {"feature": "Occupation", "instances": 145, "metric_value": 0.9294, "depth": 10}
										if obj[12]<=14:
											# {"feature": "Carryaway", "instances": 129, "metric_value": 0.9523, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Children", "instances": 65, "metric_value": 0.8717, "depth": 12}
												if obj[10]<=0:
													# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.9612, "depth": 13}
													if obj[18]<=3.0:
														# {"feature": "Age", "instances": 36, "metric_value": 0.9183, "depth": 14}
														if obj[8]<=6:
															# {"feature": "Bar", "instances": 35, "metric_value": 0.8981, "depth": 15}
															if obj[14]<=3.0:
																# {"feature": "Gender", "instances": 34, "metric_value": 0.874, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Income", "instances": 21, "metric_value": 0.7919, "depth": 17}
																	if obj[13]>1:
																		# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 18}
																		if obj[11]>0:
																			# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 19}
																			if obj[20]<=1:
																				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 8, "metric_value": 0.9544, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[20]>1:
																				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[11]<=0:
																			# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 19}
																			if obj[20]<=1:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[20]>1:
																				return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[13]<=1:
																		return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 17}
																	if obj[13]<=5:
																		# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 18}
																		if obj[20]<=1:
																			# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 19}
																			if obj[11]>1:
																				# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[11]<=1:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[20]>1:
																			return 'True'
																		else: return 'True'
																	elif obj[13]>5:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[14]>3.0:
																return 'False'
															else: return 'False'
														elif obj[8]>6:
															return 'False'
														else: return 'False'
													elif obj[18]>3.0:
														return 'False'
													else: return 'False'
												elif obj[10]>0:
													# {"feature": "Bar", "instances": 26, "metric_value": 0.6194, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 14}
														if obj[11]>1:
															# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 15}
															if obj[20]<=1:
																return 'True'
															elif obj[20]>1:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[11]<=1:
															# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 15}
															if obj[8]>1:
																# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[13]>4:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[18]<=1.0:
																			return 'True'
																		elif obj[18]>1.0:
																			return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		return 'False'
																	else: return 'False'
																elif obj[13]<=4:
																	return 'True'
																else: return 'True'
															elif obj[8]<=1:
																return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[14]>1.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[16]<=2.0:
												# {"feature": "Income", "instances": 64, "metric_value": 0.9937, "depth": 12}
												if obj[13]<=7:
													# {"feature": "Bar", "instances": 61, "metric_value": 0.9983, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.9965, "depth": 14}
														if obj[18]>0.0:
															# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 15}
															if obj[20]<=1:
																# {"feature": "Age", "instances": 28, "metric_value": 0.9059, "depth": 16}
																if obj[8]<=4:
																	# {"feature": "Children", "instances": 22, "metric_value": 0.8454, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 18}
																		if obj[11]<=3:
																			# {"feature": "Gender", "instances": 12, "metric_value": 0.65, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 7, "metric_value": 0.5917, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[11]>3:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[7]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[10]>0:
																		# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[11]>2:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[8]>4:
																	# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[11]<=2:
																			return 'False'
																		elif obj[11]>2:
																			return 'True'
																		else: return 'True'
																	elif obj[10]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[20]>1:
																# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[11]<=3:
																		return 'True'
																	elif obj[11]>3:
																		return 'False'
																	else: return 'False'
																elif obj[7]<=0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[18]<=0.0:
															# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 15}
															if obj[10]<=0:
																return 'True'
															elif obj[10]>0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]>0:
																	return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													elif obj[14]>1.0:
														# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 14}
														if obj[18]>0.0:
															# {"feature": "Age", "instances": 14, "metric_value": 0.5917, "depth": 15}
															if obj[8]<=1:
																# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 16}
																if obj[11]>1:
																	# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[20]<=1:
																		# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[20]>1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			return 'True'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[11]<=1:
																	return 'True'
																else: return 'True'
															elif obj[8]>1:
																return 'True'
															else: return 'True'
														elif obj[18]<=0.0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[13]>7:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]>14:
											# {"feature": "Carryaway", "instances": 16, "metric_value": 0.5436, "depth": 11}
											if obj[16]>1.0:
												return 'True'
											elif obj[16]<=1.0:
												# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7]>0:
													return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[17]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[9]>2:
									# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[14]<=1.0:
										return 'False'
									elif obj[14]>1.0:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]<=0:
											return 'False'
										elif obj[7]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[3]<=55:
								# {"feature": "Occupation", "instances": 82, "metric_value": 0.965, "depth": 8}
								if obj[12]>4:
									# {"feature": "Restaurant20to50", "instances": 62, "metric_value": 0.997, "depth": 9}
									if obj[18]<=2.0:
										# {"feature": "Restaurantlessthan20", "instances": 54, "metric_value": 0.9751, "depth": 10}
										if obj[17]<=3.0:
											# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 11}
											if obj[20]>1:
												# {"feature": "Age", "instances": 29, "metric_value": 0.8936, "depth": 12}
												if obj[8]<=4:
													# {"feature": "Income", "instances": 25, "metric_value": 0.9427, "depth": 13}
													if obj[13]<=7:
														# {"feature": "Carryaway", "instances": 23, "metric_value": 0.8865, "depth": 14}
														if obj[16]<=3.0:
															# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 15}
															if obj[11]>1:
																# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.7219, "depth": 16}
																if obj[9]>0:
																	# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 17}
																	if obj[14]<=1.0:
																		# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[2]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[14]>1.0:
																		return 'False'
																	else: return 'False'
																elif obj[9]<=0:
																	return 'False'
																else: return 'False'
															elif obj[11]<=1:
																# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[14]<=2.0:
																	return 'True'
																elif obj[14]>2.0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[16]>3.0:
															return 'False'
														else: return 'False'
													elif obj[13]>7:
														return 'True'
													else: return 'True'
												elif obj[8]>4:
													return 'False'
												else: return 'False'
											elif obj[20]<=1:
												# {"feature": "Income", "instances": 22, "metric_value": 0.976, "depth": 12}
												if obj[13]<=5:
													# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 13}
													if obj[11]<=1:
														# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[7]>0:
															# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[8]<=2:
																# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[9]<=3:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=1:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=0.0:
																					# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[16]<=2.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[9]>3:
																	return 'False'
																else: return 'False'
															elif obj[8]>2:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															# {"feature": "Carryaway", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[16]>2.0:
																return 'True'
															elif obj[16]<=2.0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[11]>1:
														return 'True'
													else: return 'True'
												elif obj[13]>5:
													# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 13}
													if obj[9]>0:
														# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[7]>0:
															# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[8]<=4:
																return 'False'
															elif obj[8]>4:
																return 'True'
															else: return 'True'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													elif obj[9]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[17]>3.0:
											return 'False'
										else: return 'False'
									elif obj[18]>2.0:
										# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[17]>2.0:
											return 'True'
										elif obj[17]<=2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=4:
									# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.6098, "depth": 9}
									if obj[17]>1.0:
										# {"feature": "Bar", "instances": 17, "metric_value": 0.3228, "depth": 10}
										if obj[14]<=2.0:
											return 'False'
										elif obj[14]>2.0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=0:
												return 'True'
											elif obj[7]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[17]<=1.0:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=4:
											return 'True'
										elif obj[8]>4:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[15]<=0.0:
							# {"feature": "Weather", "instances": 82, "metric_value": 0.8561, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Carryaway", "instances": 61, "metric_value": 0.9288, "depth": 8}
								if obj[16]>0.0:
									# {"feature": "Occupation", "instances": 58, "metric_value": 0.8936, "depth": 9}
									if obj[12]<=12:
										# {"feature": "Income", "instances": 47, "metric_value": 0.785, "depth": 10}
										if obj[13]>3:
											# {"feature": "Education", "instances": 30, "metric_value": 0.9183, "depth": 11}
											if obj[11]>1:
												# {"feature": "Distance", "instances": 19, "metric_value": 0.7425, "depth": 12}
												if obj[20]<=1:
													# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 13}
													if obj[8]<=4:
														# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[9]>0:
															# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 15}
															if obj[18]<=1.0:
																# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[14]<=1.0:
																	# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[17]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[14]>1.0:
																	return 'False'
																else: return 'False'
															elif obj[18]>1.0:
																return 'True'
															else: return 'True'
														elif obj[9]<=0:
															return 'False'
														else: return 'False'
													elif obj[8]>4:
														# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[7]<=0:
															# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[1]<=1:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=80:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=0.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=3.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[7]>0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[20]>1:
													return 'False'
												else: return 'False'
											elif obj[11]<=1:
												# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 12}
												if obj[1]>0:
													# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[8]>0:
														# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[7]>0:
															# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[18]>0.0:
																# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[17]<=2.0:
																	return 'True'
																elif obj[17]>2.0:
																	return 'False'
																else: return 'False'
															elif obj[18]<=0.0:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															return 'False'
														else: return 'False'
													elif obj[8]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[13]<=3:
											# {"feature": "Education", "instances": 17, "metric_value": 0.3228, "depth": 11}
											if obj[11]>0:
												return 'False'
											elif obj[11]<=0:
												# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[8]<=3:
													return 'False'
												elif obj[8]>3:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[12]>12:
										# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[8]<=6:
												return 'True'
											elif obj[8]>6:
												# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=80:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7]<=1:
															# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13]<=4:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=2.0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=2.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>2:
											# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[14]<=1.0:
												return 'False'
											elif obj[14]>1.0:
												# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=80:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7]<=0:
															# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[8]<=0:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[13]<=4:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[16]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[2]>0:
								# {"feature": "Age", "instances": 21, "metric_value": 0.4537, "depth": 8}
								if obj[8]<=2:
									return 'False'
								elif obj[8]>2:
									# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Income", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[13]<=3:
											# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[16]>0.0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=1:
														# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[12]<=7:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=0.0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[16]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										elif obj[13]>3:
											return 'True'
										else: return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=0:
						# {"feature": "Bar", "instances": 103, "metric_value": 0.623, "depth": 6}
						if obj[14]<=3.0:
							# {"feature": "Income", "instances": 98, "metric_value": 0.5647, "depth": 7}
							if obj[13]>0:
								# {"feature": "Occupation", "instances": 82, "metric_value": 0.4612, "depth": 8}
								if obj[12]>3:
									# {"feature": "Carryaway", "instances": 64, "metric_value": 0.5436, "depth": 9}
									if obj[16]<=3.0:
										# {"feature": "Maritalstatus", "instances": 57, "metric_value": 0.5852, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Restaurantlessthan20", "instances": 38, "metric_value": 0.6892, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Age", "instances": 31, "metric_value": 0.7706, "depth": 12}
												if obj[8]<=6:
													# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.8256, "depth": 13}
													if obj[15]>-1.0:
														# {"feature": "Gender", "instances": 25, "metric_value": 0.8555, "depth": 14}
														if obj[7]>0:
															# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 15}
															if obj[11]>1:
																# {"feature": "Children", "instances": 11, "metric_value": 0.8454, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 17}
																	if obj[18]<=1.0:
																		# {"feature": "Temperature", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[3]>30:
																			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[3]<=30:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[18]>1.0:
																		return 'True'
																	else: return 'True'
																elif obj[10]>0:
																	return 'True'
																else: return 'True'
															elif obj[11]<=1:
																return 'True'
															else: return 'True'
														elif obj[7]<=0:
															# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 15}
															if obj[11]>1:
																# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[10]>0:
																	return 'True'
																elif obj[10]<=0:
																	return 'False'
																else: return 'False'
															elif obj[11]<=1:
																# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[20]>1:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[20]<=1:
																		return 'True'
																	else: return 'True'
																elif obj[10]>0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[15]<=-1.0:
														return 'True'
													else: return 'True'
												elif obj[8]>6:
													return 'True'
												else: return 'True'
											elif obj[17]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[9]>1:
											# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.2975, "depth": 11}
											if obj[15]>0.0:
												return 'True'
											elif obj[15]<=0.0:
												# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[8]<=4:
													return 'True'
												elif obj[8]>4:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[16]>3.0:
										return 'True'
									else: return 'True'
								elif obj[12]<=3:
									return 'True'
								else: return 'True'
							elif obj[13]<=0:
								# {"feature": "Age", "instances": 16, "metric_value": 0.896, "depth": 8}
								if obj[8]<=3:
									# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 9}
									if obj[12]<=9:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[15]<=3.0:
											# {"feature": "Carryaway", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[16]>1.0:
												# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[20]>1:
													return 'True'
												elif obj[20]<=1:
													return 'False'
												else: return 'False'
											elif obj[16]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[15]>3.0:
											return 'False'
										else: return 'False'
									elif obj[12]>9:
										return 'True'
									else: return 'True'
								elif obj[8]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[14]>3.0:
							# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[12]>2:
								# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]>0:
									return 'True'
								elif obj[11]<=0:
									return 'False'
								else: return 'False'
							elif obj[12]<=2:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[19]<=0:
					# {"feature": "Passanger", "instances": 422, "metric_value": 0.8881, "depth": 5}
					if obj[1]>0:
						# {"feature": "Education", "instances": 408, "metric_value": 0.8709, "depth": 6}
						if obj[11]>1:
							# {"feature": "Occupation", "instances": 222, "metric_value": 0.7929, "depth": 7}
							if obj[12]<=13.270074908743435:
								# {"feature": "Children", "instances": 194, "metric_value": 0.7136, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Coffeehouse", "instances": 113, "metric_value": 0.6109, "depth": 9}
									if obj[15]<=2.0:
										# {"feature": "Age", "instances": 86, "metric_value": 0.4836, "depth": 10}
										if obj[8]>1:
											# {"feature": "Restaurantlessthan20", "instances": 50, "metric_value": 0.3274, "depth": 11}
											if obj[17]<=2.0:
												# {"feature": "Distance", "instances": 26, "metric_value": 0.5159, "depth": 12}
												if obj[20]>2:
													# {"feature": "Income", "instances": 16, "metric_value": 0.6962, "depth": 13}
													if obj[13]<=4:
														# {"feature": "Temperature", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[2]<=1:
																# {"feature": "Carryaway", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[16]<=3.0:
																	# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[9]<=1:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]>0.0:
																				return 'True'
																			elif obj[18]<=0.0:
																				return 'False'
																			else: return 'False'
																		elif obj[9]>1:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[16]>3.0:
																	return 'False'
																else: return 'False'
															elif obj[2]>1:
																return 'False'
															else: return 'False'
														elif obj[3]>55:
															return 'False'
														else: return 'False'
													elif obj[13]>4:
														return 'False'
													else: return 'False'
												elif obj[20]<=2:
													return 'False'
												else: return 'False'
											elif obj[17]>2.0:
												return 'False'
											else: return 'False'
										elif obj[8]<=1:
											# {"feature": "Temperature", "instances": 36, "metric_value": 0.65, "depth": 11}
											if obj[3]<=55:
												# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.4138, "depth": 12}
												if obj[18]<=1.0:
													return 'False'
												elif obj[18]>1.0:
													# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[14]>0.0:
														return 'False'
													elif obj[14]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[3]>55:
												# {"feature": "Income", "instances": 12, "metric_value": 0.9183, "depth": 12}
												if obj[13]>0:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[7]>0:
														# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[17]>1.0:
															# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[9]<=1:
																return 'True'
															elif obj[9]>1:
																return 'False'
															else: return 'False'
														elif obj[17]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[7]<=0:
														return 'False'
													else: return 'False'
												elif obj[13]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[15]>2.0:
										# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.8767, "depth": 10}
										if obj[18]>0.0:
											# {"feature": "Weather", "instances": 25, "metric_value": 0.795, "depth": 11}
											if obj[2]<=1:
												# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.8997, "depth": 12}
												if obj[9]>0:
													# {"feature": "Income", "instances": 15, "metric_value": 0.971, "depth": 13}
													if obj[13]>1:
														# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 14}
														if obj[14]>1.0:
															# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[16]<=3.0:
																# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		return 'False'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		return 'False'
																	elif obj[7]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[16]>3.0:
																return 'False'
															else: return 'False'
														elif obj[14]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[13]<=1:
														# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[17]>3.0:
															# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[20]<=2:
																return 'False'
															elif obj[20]>2:
																return 'True'
															else: return 'True'
														elif obj[17]<=3.0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[9]<=0:
													return 'False'
												else: return 'False'
											elif obj[2]>1:
												return 'False'
											else: return 'False'
										elif obj[18]<=0.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[10]>0:
									# {"feature": "Income", "instances": 81, "metric_value": 0.8256, "depth": 9}
									if obj[13]<=5:
										# {"feature": "Restaurantlessthan20", "instances": 53, "metric_value": 0.9052, "depth": 10}
										if obj[17]<=2.0:
											# {"feature": "Distance", "instances": 32, "metric_value": 0.9745, "depth": 11}
											if obj[20]>1:
												# {"feature": "Age", "instances": 30, "metric_value": 0.9481, "depth": 12}
												if obj[8]>0:
													# {"feature": "Carryaway", "instances": 26, "metric_value": 0.9829, "depth": 13}
													if obj[16]>1.0:
														# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9457, "depth": 14}
														if obj[18]>0.0:
															# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.9819, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9641, "depth": 16}
																if obj[15]>-1.0:
																	# {"feature": "Weather", "instances": 17, "metric_value": 0.9774, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 18}
																		if obj[14]>0.0:
																			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 19}
																			if obj[4]<=1:
																				return 'False'
																			elif obj[4]>1:
																				return 'True'
																			else: return 'True'
																		elif obj[14]<=0.0:
																			return 'True'
																		else: return 'True'
																	elif obj[2]>0:
																		# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 18}
																		if obj[4]>1:
																			# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[3]<=30:
																				# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[7]<=1:
																					# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[14]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[4]<=1:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[15]<=-1.0:
																	return 'False'
																else: return 'False'
															elif obj[9]>1:
																return 'True'
															else: return 'True'
														elif obj[18]<=0.0:
															return 'False'
														else: return 'False'
													elif obj[16]<=1.0:
														# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[2]>0:
															return 'True'
														elif obj[2]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[8]<=0:
													return 'False'
												else: return 'False'
											elif obj[20]<=1:
												return 'True'
											else: return 'True'
										elif obj[17]>2.0:
											# {"feature": "Age", "instances": 21, "metric_value": 0.7025, "depth": 11}
											if obj[8]<=2:
												# {"feature": "Gender", "instances": 13, "metric_value": 0.8905, "depth": 12}
												if obj[7]<=0:
													# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[4]>0:
														return 'False'
													elif obj[4]<=0:
														# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[14]>0.0:
															return 'True'
														elif obj[14]<=0.0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[7]>0:
													# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[15]<=2.0:
														return 'True'
													elif obj[15]>2.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[8]>2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[13]>5:
										# {"feature": "Age", "instances": 28, "metric_value": 0.5917, "depth": 10}
										if obj[8]<=3:
											# {"feature": "Bar", "instances": 19, "metric_value": 0.2975, "depth": 11}
											if obj[14]<=1.0:
												return 'False'
											elif obj[14]>1.0:
												# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]>55:
													return 'False'
												elif obj[3]<=55:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[8]>3:
											# {"feature": "Temperature", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=55:
												# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[15]>0.0:
													return 'False'
												elif obj[15]<=0.0:
													# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2]<=1:
														return 'True'
													elif obj[2]>1:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[3]>55:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7]>0:
													return 'True'
												elif obj[7]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[12]>13.270074908743435:
								# {"feature": "Bar", "instances": 28, "metric_value": 0.9963, "depth": 8}
								if obj[14]<=2.0:
									# {"feature": "Coffeehouse", "instances": 24, "metric_value": 0.9544, "depth": 9}
									if obj[15]<=3.0:
										# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.8813, "depth": 10}
										if obj[18]<=1.0:
											# {"feature": "Age", "instances": 14, "metric_value": 0.9852, "depth": 11}
											if obj[8]>1:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[7]>0:
													# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[2]<=0:
														# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[20]>1:
															return 'True'
														elif obj[20]<=1:
															return 'False'
														else: return 'False'
													elif obj[2]>0:
														return 'False'
													else: return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											elif obj[8]<=1:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[20]>1:
													return 'False'
												elif obj[20]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[18]>1.0:
											return 'True'
										else: return 'True'
									elif obj[15]>3.0:
										# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[2]>0:
											return 'False'
										elif obj[2]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]<=1:
												return 'True'
											elif obj[8]>1:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[14]>2.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=1:
							# {"feature": "Gender", "instances": 186, "metric_value": 0.9383, "depth": 7}
							if obj[7]>0:
								# {"feature": "Income", "instances": 99, "metric_value": 0.782, "depth": 8}
								if obj[13]>1:
									# {"feature": "Coffeehouse", "instances": 87, "metric_value": 0.8333, "depth": 9}
									if obj[15]<=2.0:
										# {"feature": "Restaurantlessthan20", "instances": 73, "metric_value": 0.7587, "depth": 10}
										if obj[17]<=2.0:
											# {"feature": "Maritalstatus", "instances": 51, "metric_value": 0.8479, "depth": 11}
											if obj[9]<=2:
												# {"feature": "Occupation", "instances": 46, "metric_value": 0.8865, "depth": 12}
												if obj[12]<=19:
													# {"feature": "Age", "instances": 43, "metric_value": 0.9103, "depth": 13}
													if obj[8]>1:
														# {"feature": "Children", "instances": 29, "metric_value": 0.7973, "depth": 14}
														if obj[10]>0:
															# {"feature": "Time", "instances": 23, "metric_value": 0.8865, "depth": 15}
															if obj[4]<=1:
																# {"feature": "Weather", "instances": 20, "metric_value": 0.9341, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 17}
																	if obj[18]<=1.0:
																		# {"feature": "Temperature", "instances": 11, "metric_value": 0.684, "depth": 18}
																		if obj[3]<=55:
																			# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 19}
																			if obj[14]>0.0:
																				# {"feature": "Carryaway", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[16]>1.0:
																					return 'False'
																				elif obj[16]<=1.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]>2:
																						return 'False'
																					elif obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'False'
																			elif obj[14]<=0.0:
																				return 'True'
																			else: return 'True'
																		elif obj[3]>55:
																			return 'False'
																		else: return 'False'
																	elif obj[18]>1.0:
																		# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[3]<=55:
																			# {"feature": "Carryaway", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[16]>1.0:
																				return 'False'
																			elif obj[16]<=1.0:
																				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[20]<=2:
																					return 'False'
																				elif obj[20]>2:
																					return 'True'
																				else: return 'True'
																			else: return 'False'
																		elif obj[3]>55:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																elif obj[2]>0:
																	# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[14]>0.0:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=55:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=3.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=3:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[14]<=0.0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[4]>1:
																return 'False'
															else: return 'False'
														elif obj[10]<=0:
															return 'False'
														else: return 'False'
													elif obj[8]<=1:
														# {"feature": "Weather", "instances": 14, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 15}
															if obj[4]<=1:
																# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 16}
																if obj[20]>1:
																	# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 17}
																	if obj[18]<=1.0:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=2.0:
																					return 'False'
																				elif obj[16]>2.0:
																					return 'True'
																				else: return 'True'
																			elif obj[3]>55:
																				return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[18]>1.0:
																		return 'False'
																	else: return 'False'
																elif obj[20]<=1:
																	# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[18]>0.0:
																		return 'True'
																	elif obj[18]<=0.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[4]>1:
																return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[12]>19:
													return 'False'
												else: return 'False'
											elif obj[9]>2:
												return 'False'
											else: return 'False'
										elif obj[17]>2.0:
											# {"feature": "Carryaway", "instances": 22, "metric_value": 0.4395, "depth": 11}
											if obj[16]>-1.0:
												# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.2762, "depth": 12}
												if obj[18]>0.0:
													return 'False'
												elif obj[18]<=0.0:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=55:
														return 'True'
													elif obj[3]>55:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]<=-1.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[15]>2.0:
										# {"feature": "Weather", "instances": 14, "metric_value": 1.0, "depth": 10}
										if obj[2]<=0:
											# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[18]>0.0:
												# {"feature": "Bar", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[14]<=3.0:
													return 'True'
												elif obj[14]>3.0:
													return 'False'
												else: return 'False'
											elif obj[18]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[2]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]<=1:
									return 'False'
								else: return 'False'
							elif obj[7]<=0:
								# {"feature": "Income", "instances": 87, "metric_value": 0.9999, "depth": 8}
								if obj[13]>0:
									# {"feature": "Bar", "instances": 80, "metric_value": 0.9959, "depth": 9}
									if obj[14]<=2.0:
										# {"feature": "Maritalstatus", "instances": 71, "metric_value": 0.9999, "depth": 10}
										if obj[9]<=3:
											# {"feature": "Distance", "instances": 68, "metric_value": 0.9994, "depth": 11}
											if obj[20]>2:
												# {"feature": "Coffeehouse", "instances": 43, "metric_value": 0.9682, "depth": 12}
												if obj[15]<=3.0:
													# {"feature": "Carryaway", "instances": 42, "metric_value": 0.9587, "depth": 13}
													if obj[16]>0.0:
														# {"feature": "Children", "instances": 40, "metric_value": 0.971, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 1.0, "depth": 15}
															if obj[18]<=1.0:
																# {"feature": "Age", "instances": 21, "metric_value": 0.9852, "depth": 16}
																if obj[8]>0:
																	# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 17}
																	if obj[12]>1:
																		# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.9403, "depth": 18}
																		if obj[17]<=2.0:
																			# {"feature": "Temperature", "instances": 13, "metric_value": 0.9612, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Weather", "instances": 8, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=1:
																					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[4]<=1:
																						return 'True'
																					else: return 'True'
																				elif obj[2]>1:
																					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[4]<=1:
																						return 'False'
																					elif obj[4]>1:
																						return 'True'
																					else: return 'True'
																				else: return 'False'
																			elif obj[3]>55:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[4]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[17]>2.0:
																			return 'False'
																		else: return 'False'
																	elif obj[12]<=1:
																		# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[3]<=55:
																			return 'True'
																		elif obj[3]>55:
																			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[4]<=0:
																					# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[17]<=1.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[8]<=0:
																	return 'False'
																else: return 'False'
															elif obj[18]>1.0:
																return 'True'
															else: return 'True'
														elif obj[10]>0:
															# {"feature": "Age", "instances": 16, "metric_value": 0.8113, "depth": 15}
															if obj[8]>1:
																# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 16}
																if obj[18]>0.0:
																	# {"feature": "Weather", "instances": 8, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 18}
																		if obj[12]>1:
																			# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[4]<=1:
																					# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[17]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[12]<=1:
																			return 'True'
																		else: return 'True'
																	elif obj[2]>0:
																		return 'False'
																	else: return 'False'
																elif obj[18]<=0.0:
																	return 'True'
																else: return 'True'
															elif obj[8]<=1:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[16]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[15]>3.0:
													return 'False'
												else: return 'False'
											elif obj[20]<=2:
												# {"feature": "Occupation", "instances": 25, "metric_value": 0.9427, "depth": 12}
												if obj[12]>1:
													# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.8865, "depth": 13}
													if obj[17]>1.0:
														# {"feature": "Age", "instances": 19, "metric_value": 0.9495, "depth": 14}
														if obj[8]>1:
															# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 15}
															if obj[18]<=2.0:
																# {"feature": "Carryaway", "instances": 17, "metric_value": 0.874, "depth": 16}
																if obj[16]<=3.0:
																	# {"feature": "Children", "instances": 15, "metric_value": 0.9183, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 18}
																		if obj[3]<=55:
																			# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 19}
																			if obj[15]<=3.0:
																				# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[4]<=1:
																						return 'False'
																					else: return 'False'
																				elif obj[2]>0:
																					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[4]<=3:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[15]>3.0:
																				return 'False'
																			else: return 'False'
																		elif obj[3]>55:
																			return 'False'
																		else: return 'False'
																	elif obj[10]>0:
																		# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 18}
																		if obj[15]>0.0:
																			# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[3]>55:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[4]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[3]<=55:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[4]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[15]<=0.0:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[16]>3.0:
																	return 'False'
																else: return 'False'
															elif obj[18]>2.0:
																return 'True'
															else: return 'True'
														elif obj[8]<=1:
															return 'True'
														else: return 'True'
													elif obj[17]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[9]>3:
											return 'False'
										else: return 'False'
									elif obj[14]>2.0:
										# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[20]>1:
											return 'True'
										elif obj[20]<=1:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]<=1:
												return 'False'
											elif obj[8]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[13]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[8]>1:
							return 'True'
						elif obj[8]<=1:
							# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[15]<=3.0:
								return 'False'
							elif obj[15]>3.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Bar", "instances": 1404, "metric_value": 0.9865, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Children", "instances": 1003, "metric_value": 0.9451, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Weather", "instances": 515, "metric_value": 0.9911, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Income", "instances": 396, "metric_value": 0.9995, "depth": 5}
					if obj[13]<=4:
						# {"feature": "Restaurant20to50", "instances": 260, "metric_value": 0.9916, "depth": 6}
						if obj[18]>0.0:
							# {"feature": "Passanger", "instances": 185, "metric_value": 0.9643, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Coupon_validity", "instances": 160, "metric_value": 0.9863, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Age", "instances": 123, "metric_value": 0.9474, "depth": 9}
									if obj[8]<=4:
										# {"feature": "Occupation", "instances": 91, "metric_value": 0.9803, "depth": 10}
										if obj[12]>1:
											# {"feature": "Coffeehouse", "instances": 87, "metric_value": 0.9653, "depth": 11}
											if obj[15]>0.0:
												# {"feature": "Temperature", "instances": 66, "metric_value": 0.9024, "depth": 12}
												if obj[3]<=55:
													# {"feature": "Restaurantlessthan20", "instances": 36, "metric_value": 0.9799, "depth": 13}
													if obj[17]>1.0:
														# {"feature": "Maritalstatus", "instances": 33, "metric_value": 0.9457, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Education", "instances": 30, "metric_value": 0.9183, "depth": 15}
															if obj[11]<=2:
																# {"feature": "Gender", "instances": 28, "metric_value": 0.8631, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9183, "depth": 17}
																	if obj[19]<=0:
																		# {"feature": "Carryaway", "instances": 18, "metric_value": 0.9641, "depth": 18}
																		if obj[16]>1.0:
																			# {"feature": "Driving_to", "instances": 16, "metric_value": 0.9887, "depth": 19}
																			if obj[0]>0:
																				# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 20}
																				if obj[20]>1:
																					# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 21}
																					if obj[4]<=1:
																						return 'False'
																					elif obj[4]>1:
																						return 'True'
																					else: return 'True'
																				elif obj[20]<=1:
																					return 'False'
																				else: return 'False'
																			elif obj[0]<=0:
																				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[20]<=1:
																					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[4]>2:
																						return 'True'
																					elif obj[4]<=2:
																						return 'True'
																					else: return 'True'
																				elif obj[20]>1:
																					return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[16]<=1.0:
																			return 'True'
																		else: return 'True'
																	elif obj[19]>0:
																		return 'True'
																	else: return 'True'
																elif obj[7]<=0:
																	# {"feature": "Carryaway", "instances": 7, "metric_value": 0.5917, "depth": 17}
																	if obj[16]>1.0:
																		return 'True'
																	elif obj[16]<=1.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[11]>2:
																return 'False'
															else: return 'False'
														elif obj[9]>1:
															# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]<=0:
																return 'False'
															elif obj[7]>0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[17]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[3]>55:
													# {"feature": "Carryaway", "instances": 30, "metric_value": 0.7219, "depth": 13}
													if obj[16]<=3.0:
														# {"feature": "Driving_to", "instances": 26, "metric_value": 0.7793, "depth": 14}
														if obj[0]>0:
															# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 15}
															if obj[11]<=2:
																# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 16}
																if obj[20]>1:
																	# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9911, "depth": 17}
																	if obj[9]>0:
																		# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 18}
																		if obj[17]>1.0:
																			# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[4]<=1:
																				# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[7]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[4]>1:
																				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[7]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[17]<=1.0:
																			return 'False'
																		else: return 'False'
																	elif obj[9]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[20]<=1:
																	# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[9]>0:
																		return 'True'
																	elif obj[9]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[11]>2:
																return 'True'
															else: return 'True'
														elif obj[0]<=0:
															# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 15}
															if obj[11]<=2:
																return 'True'
															elif obj[11]>2:
																# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[4]<=2:
																	return 'True'
																elif obj[4]>2:
																	# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[17]<=-1.0:
																		return 'True'
																	elif obj[17]>-1.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[16]>3.0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[15]<=0.0:
												# {"feature": "Time", "instances": 21, "metric_value": 0.9587, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 13}
													if obj[20]<=2:
														# {"feature": "Carryaway", "instances": 12, "metric_value": 0.9183, "depth": 14}
														if obj[16]>1.0:
															# {"feature": "Driving_to", "instances": 9, "metric_value": 0.7642, "depth": 15}
															if obj[0]<=1:
																# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[11]<=0:
																		# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=30:
																				return 'True'
																			elif obj[3]>30:
																				return 'False'
																			else: return 'False'
																		elif obj[9]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[11]>0:
																		return 'False'
																	else: return 'False'
																elif obj[7]>0:
																	return 'True'
																else: return 'True'
															elif obj[0]>1:
																return 'True'
															else: return 'True'
														elif obj[16]<=1.0:
															# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[19]>0:
																return 'False'
															elif obj[19]<=0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[20]>2:
														return 'False'
													else: return 'False'
												elif obj[4]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[12]<=1:
											return 'False'
										else: return 'False'
									elif obj[8]>4:
										# {"feature": "Time", "instances": 32, "metric_value": 0.7579, "depth": 10}
										if obj[4]>0:
											# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.9495, "depth": 11}
											if obj[9]>0:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 12}
												if obj[19]<=0:
													# {"feature": "Restaurantlessthan20", "instances": 15, "metric_value": 0.7219, "depth": 13}
													if obj[17]>1.0:
														# {"feature": "Temperature", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[3]>55:
															# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[11]<=0:
																# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[12]<=7:
																	# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[0]<=0:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[0]>0:
																		return 'False'
																	else: return 'False'
																elif obj[12]>7:
																	return 'True'
																else: return 'True'
															elif obj[11]>0:
																return 'True'
															else: return 'True'
														elif obj[3]<=55:
															return 'True'
														else: return 'True'
													elif obj[17]<=1.0:
														return 'True'
													else: return 'True'
												elif obj[19]>0:
													return 'False'
												else: return 'False'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[6]>0:
									# {"feature": "Restaurantlessthan20", "instances": 37, "metric_value": 0.9353, "depth": 9}
									if obj[17]>1.0:
										# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.8238, "depth": 10}
										if obj[15]<=2.0:
											# {"feature": "Carryaway", "instances": 25, "metric_value": 0.9044, "depth": 11}
											if obj[16]>1.0:
												# {"feature": "Time", "instances": 20, "metric_value": 0.971, "depth": 12}
												if obj[4]<=0:
													# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.7219, "depth": 13}
													if obj[9]<=0:
														return 'False'
													elif obj[9]>0:
														# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[3]>55:
															return 'True'
														elif obj[3]<=55:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[4]>0:
													# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[8]<=5:
														# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[11]<=3:
															# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[7]>0:
																# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[12]<=6:
																	# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[0]<=0:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[9]>0:
																		return 'False'
																	else: return 'False'
																elif obj[12]>6:
																	return 'True'
																else: return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														elif obj[11]>3:
															return 'True'
														else: return 'True'
													elif obj[8]>5:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[16]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[15]>2.0:
											return 'False'
										else: return 'False'
									elif obj[17]<=1.0:
										# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[11]<=2:
											return 'True'
										elif obj[11]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[1]>1:
								# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.5294, "depth": 8}
								if obj[15]>0.0:
									# {"feature": "Age", "instances": 23, "metric_value": 0.258, "depth": 9}
									if obj[8]>0:
										return 'True'
									elif obj[8]<=0:
										return 'False'
									else: return 'False'
								elif obj[15]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[18]<=0.0:
							# {"feature": "Occupation", "instances": 75, "metric_value": 0.9782, "depth": 7}
							if obj[12]>1:
								# {"feature": "Age", "instances": 69, "metric_value": 0.9926, "depth": 8}
								if obj[8]<=4:
									# {"feature": "Maritalstatus", "instances": 55, "metric_value": 0.9979, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 28, "metric_value": 0.8631, "depth": 10}
										if obj[19]<=0:
											# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 11}
											if obj[11]<=3:
												# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 1.0, "depth": 12}
												if obj[17]>0.0:
													# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9612, "depth": 13}
													if obj[6]<=0:
														# {"feature": "Driving_to", "instances": 10, "metric_value": 1.0, "depth": 14}
														if obj[0]>0:
															# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[15]>1.0:
																# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		return 'True'
																	elif obj[7]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[3]>55:
																	return 'False'
																else: return 'False'
															elif obj[15]<=1.0:
																return 'False'
															else: return 'False'
														elif obj[0]<=0:
															# {"feature": "Carryaway", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[16]>2.0:
																return 'True'
															elif obj[16]<=2.0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[6]>0:
														return 'False'
													else: return 'False'
												elif obj[17]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[11]>3:
												return 'True'
											else: return 'True'
										elif obj[19]>0:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										# {"feature": "Gender", "instances": 27, "metric_value": 0.9183, "depth": 10}
										if obj[7]>0:
											# {"feature": "Coupon_validity", "instances": 19, "metric_value": 0.998, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.8905, "depth": 12}
												if obj[17]<=2.0:
													# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[3]>30:
														# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[1]>0:
															# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[4]>0:
																# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[11]>0:
																	return 'False'
																elif obj[11]<=0:
																	# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=0.0:
																		return 'True'
																	elif obj[15]>0.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[4]<=0:
																return 'True'
															else: return 'True'
														elif obj[1]<=0:
															return 'True'
														else: return 'True'
													elif obj[3]<=30:
														return 'False'
													else: return 'False'
												elif obj[17]>2.0:
													return 'False'
												else: return 'False'
											elif obj[6]>0:
												# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[11]<=0:
													return 'True'
												elif obj[11]>0:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[15]>1.0:
														return 'True'
													elif obj[15]<=1.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[8]>4:
									# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 9}
									if obj[20]>1:
										# {"feature": "Driving_to", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[0]>0:
											# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[16]<=3.0:
												# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[3]<=55:
													return 'False'
												elif obj[3]>55:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]>0:
														return 'True'
													elif obj[7]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]>3.0:
												return 'True'
											else: return 'True'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									elif obj[20]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[12]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[13]>4:
						# {"feature": "Education", "instances": 136, "metric_value": 0.9429, "depth": 6}
						if obj[11]>1:
							# {"feature": "Restaurant20to50", "instances": 76, "metric_value": 0.8504, "depth": 7}
							if obj[18]>0.0:
								# {"feature": "Maritalstatus", "instances": 56, "metric_value": 0.9241, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Age", "instances": 45, "metric_value": 0.971, "depth": 9}
									if obj[8]<=5:
										# {"feature": "Passanger", "instances": 42, "metric_value": 0.9852, "depth": 10}
										if obj[1]>0:
											# {"feature": "Occupation", "instances": 32, "metric_value": 1.0, "depth": 11}
											if obj[12]<=12:
												# {"feature": "Carryaway", "instances": 30, "metric_value": 0.9968, "depth": 12}
												if obj[16]>1.0:
													# {"feature": "Time", "instances": 24, "metric_value": 0.995, "depth": 13}
													if obj[4]>0:
														# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 14}
														if obj[19]<=0:
															# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 15}
															if obj[15]<=1.0:
																# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[6]<=0:
																	# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[0]>0:
																		# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[17]>2.0:
																			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[7]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[17]<=2.0:
																			return 'False'
																		else: return 'False'
																	elif obj[0]<=0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=2.0:
																			return 'True'
																		elif obj[17]>2.0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[6]>0:
																	return 'False'
																else: return 'False'
															elif obj[15]>1.0:
																# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[0]<=0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]>1.0:
																			return 'True'
																		elif obj[17]<=1.0:
																			return 'False'
																		else: return 'False'
																	elif obj[0]>0:
																		return 'False'
																	else: return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[19]>0:
															return 'False'
														else: return 'False'
													elif obj[4]<=0:
														# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[17]<=2.0:
															# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[15]>1.0:
																# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[19]>0:
																		return 'False'
																	elif obj[19]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	return 'True'
																else: return 'True'
															elif obj[15]<=1.0:
																return 'False'
															else: return 'False'
														elif obj[17]>2.0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[16]<=1.0:
													# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[17]<=1.0:
														return 'True'
													elif obj[17]>1.0:
														# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[0]<=0:
															return 'False'
														elif obj[0]>0:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											elif obj[12]>12:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.7219, "depth": 11}
											if obj[15]<=0.0:
												# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[16]<=2.0:
													# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[17]>1.0:
														return 'True'
													elif obj[17]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[16]>2.0:
													return 'False'
												else: return 'False'
											elif obj[15]>0.0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[8]>5:
										return 'False'
									else: return 'False'
								elif obj[9]>1:
									# {"feature": "Temperature", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[3]>30:
										return 'False'
									elif obj[3]<=30:
										# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[8]<=1:
											return 'False'
										elif obj[8]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[18]<=0.0:
								# {"feature": "Passanger", "instances": 20, "metric_value": 0.469, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[12]<=1:
										# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[4]>0:
											# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6]>0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7]>0:
													return 'True'
												elif obj[7]<=0:
													return 'False'
												else: return 'False'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=0:
											return 'False'
										else: return 'False'
									elif obj[12]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[11]<=1:
							# {"feature": "Driving_to", "instances": 60, "metric_value": 0.9968, "depth": 7}
							if obj[0]>0:
								# {"feature": "Occupation", "instances": 37, "metric_value": 0.9353, "depth": 8}
								if obj[12]>3:
									# {"feature": "Age", "instances": 26, "metric_value": 0.9957, "depth": 9}
									if obj[8]>0:
										# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9799, "depth": 10}
										if obj[18]<=1.0:
											# {"feature": "Carryaway", "instances": 16, "metric_value": 0.9887, "depth": 11}
											if obj[16]<=2.0:
												# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[15]<=1.0:
														return 'True'
													elif obj[15]>1.0:
														# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[19]<=0:
															# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[20]>2:
																return 'True'
															elif obj[20]<=2:
																return 'False'
															else: return 'False'
														elif obj[19]>0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[4]>1:
													return 'False'
												else: return 'False'
											elif obj[16]>2.0:
												# {"feature": "Temperature", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[3]>55:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[6]<=0:
															return 'True'
														elif obj[6]>0:
															# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[15]<=3.0:
																return 'False'
															elif obj[15]>3.0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[7]>0:
														return 'False'
													else: return 'False'
												elif obj[3]<=55:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[18]>1.0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[1]>0:
												return 'False'
											elif obj[1]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7]>0:
													return 'True'
												elif obj[7]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								elif obj[12]<=3:
									# {"feature": "Carryaway", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[16]>1.0:
										return 'False'
									elif obj[16]<=1.0:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]<=55:
											return 'False'
										elif obj[3]>55:
											# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]>0:
												return 'False'
											elif obj[4]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]<=0:
								# {"feature": "Carryaway", "instances": 23, "metric_value": 0.9321, "depth": 8}
								if obj[16]>2.0:
									# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 9}
									if obj[4]>2:
										# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 10}
										if obj[12]>2:
											# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[1]>0:
													return 'False'
												elif obj[1]<=0:
													# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9]>0:
														return 'False'
													elif obj[9]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]>4:
												return 'True'
											else: return 'True'
										elif obj[12]<=2:
											return 'False'
										else: return 'False'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								elif obj[16]<=2.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[2]>0:
					# {"feature": "Education", "instances": 119, "metric_value": 0.8844, "depth": 5}
					if obj[11]>0:
						# {"feature": "Occupation", "instances": 72, "metric_value": 0.7107, "depth": 6}
						if obj[12]<=14:
							# {"feature": "Gender", "instances": 62, "metric_value": 0.7706, "depth": 7}
							if obj[7]>0:
								# {"feature": "Income", "instances": 34, "metric_value": 0.5226, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Age", "instances": 20, "metric_value": 0.7219, "depth": 9}
									if obj[8]>1:
										# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0]>0:
												return 'True'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[8]<=1:
										# {"feature": "Driving_to", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[0]<=0:
											# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[18]<=1.0:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]>1:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[15]<=1.0:
														return 'True'
													elif obj[15]>1.0:
														return 'False'
													else: return 'False'
												elif obj[1]<=1:
													return 'False'
												else: return 'False'
											elif obj[18]>1.0:
												return 'True'
											else: return 'True'
										elif obj[0]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[13]>4:
									return 'False'
								else: return 'False'
							elif obj[7]<=0:
								# {"feature": "Income", "instances": 28, "metric_value": 0.9403, "depth": 8}
								if obj[13]>1:
									# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 9}
									if obj[8]<=5:
										# {"feature": "Time", "instances": 19, "metric_value": 0.998, "depth": 10}
										if obj[4]<=3:
											# {"feature": "Carryaway", "instances": 17, "metric_value": 0.9774, "depth": 11}
											if obj[16]<=2.0:
												# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.9968, "depth": 12}
												if obj[9]>0:
													# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[15]<=1.0:
														# {"feature": "Temperature", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[3]>30:
															# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[18]<=2.0:
																return 'False'
															elif obj[18]>2.0:
																# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[0]<=0:
																	return 'True'
																elif obj[0]>0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[3]<=30:
															# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[0]>1:
																# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[17]<=1.0:
																	return 'True'
																elif obj[17]>1.0:
																	return 'False'
																else: return 'False'
															elif obj[0]<=1:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[15]>1.0:
														return 'True'
													else: return 'True'
												elif obj[9]<=0:
													# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1]<=1:
														return 'True'
													elif obj[1]>1:
														# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[0]<=0:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=55:
																# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[6]<=1:
																	# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=2.0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=2.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]>2.0:
												return 'True'
											else: return 'True'
										elif obj[4]>3:
											return 'False'
										else: return 'False'
									elif obj[8]>5:
										return 'False'
									else: return 'False'
								elif obj[13]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[12]>14:
							return 'False'
						else: return 'False'
					elif obj[11]<=0:
						# {"feature": "Age", "instances": 47, "metric_value": 0.9971, "depth": 6}
						if obj[8]>0:
							# {"feature": "Driving_to", "instances": 39, "metric_value": 0.9881, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Income", "instances": 30, "metric_value": 0.9183, "depth": 8}
								if obj[13]>2:
									# {"feature": "Occupation", "instances": 24, "metric_value": 0.9799, "depth": 9}
									if obj[12]<=10:
										# {"feature": "Carryaway", "instances": 19, "metric_value": 0.8997, "depth": 10}
										if obj[16]<=3.0:
											# {"feature": "Time", "instances": 17, "metric_value": 0.7871, "depth": 11}
											if obj[4]<=2:
												# {"feature": "Gender", "instances": 12, "metric_value": 0.9183, "depth": 12}
												if obj[7]<=0:
													# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[20]>1:
														# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[3]<=30:
															return 'True'
														elif obj[3]>30:
															# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[15]<=0.0:
																return 'False'
															elif obj[15]>0.0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[20]<=1:
														return 'False'
													else: return 'False'
												elif obj[7]>0:
													return 'True'
												else: return 'True'
											elif obj[4]>2:
												return 'True'
											else: return 'True'
										elif obj[16]>3.0:
											return 'False'
										else: return 'False'
									elif obj[12]>10:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[20]>1:
											return 'False'
										elif obj[20]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[13]<=2:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[13]>2:
									return 'False'
								elif obj[13]<=2:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[10]>0:
				# {"feature": "Weather", "instances": 488, "metric_value": 0.8508, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Time", "instances": 346, "metric_value": 0.9053, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Temperature", "instances": 299, "metric_value": 0.9351, "depth": 6}
						if obj[3]>30:
							# {"feature": "Income", "instances": 259, "metric_value": 0.9596, "depth": 7}
							if obj[13]<=6:
								# {"feature": "Restaurant20to50", "instances": 224, "metric_value": 0.9813, "depth": 8}
								if obj[18]<=2.0:
									# {"feature": "Maritalstatus", "instances": 213, "metric_value": 0.9704, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Education", "instances": 192, "metric_value": 0.9867, "depth": 10}
										if obj[11]<=4:
											# {"feature": "Occupation", "instances": 189, "metric_value": 0.9829, "depth": 11}
											if obj[12]<=21:
												# {"feature": "Coffeehouse", "instances": 185, "metric_value": 0.9868, "depth": 12}
												if obj[15]<=2.0:
													# {"feature": "Driving_to", "instances": 156, "metric_value": 0.9957, "depth": 13}
													if obj[0]>0:
														# {"feature": "Restaurantlessthan20", "instances": 121, "metric_value": 0.9821, "depth": 14}
														if obj[17]<=3.0:
															# {"feature": "Coupon_validity", "instances": 115, "metric_value": 0.9908, "depth": 15}
															if obj[6]<=0:
																# {"feature": "Passanger", "instances": 90, "metric_value": 1.0, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Carryaway", "instances": 80, "metric_value": 0.9959, "depth": 17}
																	if obj[16]<=3.0:
																		# {"feature": "Age", "instances": 73, "metric_value": 0.9999, "depth": 18}
																		if obj[8]<=2:
																			# {"feature": "Distance", "instances": 37, "metric_value": 0.974, "depth": 19}
																			if obj[20]<=2:
																				# {"feature": "Gender", "instances": 29, "metric_value": 0.9294, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Direction_same", "instances": 24, "metric_value": 0.9544, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					elif obj[19]>0:
																						return 'False'
																					else: return 'False'
																				elif obj[7]<=0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					elif obj[19]>0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[20]>2:
																				# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[7]<=0:
																					return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[8]>2:
																			# {"feature": "Distance", "instances": 36, "metric_value": 0.9641, "depth": 19}
																			if obj[20]>1:
																				# {"feature": "Direction_same", "instances": 26, "metric_value": 0.8905, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Gender", "instances": 24, "metric_value": 0.9183, "depth": 21}
																					if obj[7]>0:
																						return 'False'
																					elif obj[7]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[19]>0:
																					return 'False'
																				else: return 'False'
																			elif obj[20]<=1:
																				# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 21}
																					if obj[19]>0:
																						return 'True'
																					elif obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[7]<=0:
																					return 'False'
																				else: return 'False'
																			else: return 'True'
																		else: return 'False'
																	elif obj[16]>3.0:
																		# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[8]>0:
																			return 'False'
																		elif obj[8]<=0:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]>0:
																				return 'True'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	else: return 'False'
																elif obj[1]>1:
																	# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 17}
																	if obj[8]<=4:
																		# {"feature": "Carryaway", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[16]>1.0:
																			return 'True'
																		elif obj[16]<=1.0:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]>0:
																				return 'False'
																			elif obj[7]<=0:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	elif obj[8]>4:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			return 'True'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																else: return 'True'
															elif obj[6]>0:
																# {"feature": "Carryaway", "instances": 25, "metric_value": 0.795, "depth": 16}
																if obj[16]>1.0:
																	# {"feature": "Gender", "instances": 17, "metric_value": 0.9367, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 18}
																		if obj[20]>1:
																			return 'False'
																		elif obj[20]<=1:
																			# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[8]>3:
																				return 'False'
																			elif obj[8]<=3:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	elif obj[7]<=0:
																		# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[8]>2:
																			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[1]<=1:
																				return 'False'
																			elif obj[1]>1:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]>0:
																					return 'True'
																				elif obj[19]<=0:
																					return 'False'
																				else: return 'False'
																			else: return 'True'
																		elif obj[8]<=2:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[16]<=1.0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[17]>3.0:
															return 'False'
														else: return 'False'
													elif obj[0]<=0:
														# {"feature": "Gender", "instances": 35, "metric_value": 0.971, "depth": 14}
														if obj[7]>0:
															# {"feature": "Passanger", "instances": 25, "metric_value": 0.9988, "depth": 15}
															if obj[1]>0:
																# {"feature": "Carryaway", "instances": 24, "metric_value": 0.995, "depth": 16}
																if obj[16]>0.0:
																	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 17}
																	if obj[8]>2:
																		# {"feature": "Distance", "instances": 15, "metric_value": 0.9968, "depth": 18}
																		if obj[20]>1:
																			# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9957, "depth": 19}
																			if obj[6]>0:
																				# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 20}
																				if obj[17]>1.0:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[17]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[6]<=0:
																				# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[20]<=1:
																			return 'True'
																		else: return 'True'
																	elif obj[8]<=2:
																		# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 18}
																		if obj[17]<=1.0:
																			# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[6]<=0:
																				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[20]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[20]>1:
																					return 'False'
																				else: return 'False'
																			elif obj[6]>0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[17]>1.0:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[16]<=0.0:
																	return 'True'
																else: return 'True'
															elif obj[1]<=0:
																return 'True'
															else: return 'True'
														elif obj[7]<=0:
															# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.469, "depth": 15}
															if obj[6]>0:
																# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[8]>2:
																	# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[16]<=1.0:
																		return 'True'
																	elif obj[16]>1.0:
																		return 'False'
																	else: return 'False'
																elif obj[8]<=2:
																	return 'True'
																else: return 'True'
															elif obj[6]<=0:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[15]>2.0:
													# {"feature": "Distance", "instances": 29, "metric_value": 0.8498, "depth": 13}
													if obj[20]<=2:
														# {"feature": "Age", "instances": 25, "metric_value": 0.9044, "depth": 14}
														if obj[8]>2:
															# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 15}
															if obj[1]<=1:
																# {"feature": "Driving_to", "instances": 8, "metric_value": 0.9544, "depth": 16}
																if obj[0]>1:
																	# {"feature": "Carryaway", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[16]>2.0:
																		return 'True'
																	elif obj[16]<=2.0:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			return 'True'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[0]<=1:
																	# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[17]<=2.0:
																		return 'False'
																	elif obj[17]>2.0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[1]>1:
																# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[6]>0:
																	# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[0]<=0:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=4.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[0]>0:
																		return 'False'
																	else: return 'False'
																elif obj[6]<=0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[8]<=2:
															# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.65, "depth": 15}
															if obj[17]<=2.0:
																return 'False'
															elif obj[17]>2.0:
																# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[0]<=0:
																		# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[6]>0:
																			return 'False'
																		elif obj[6]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[0]>0:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=1:
																	return 'False'
																else: return 'False'
															else: return 'True'
														else: return 'False'
													elif obj[20]>2:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>21:
												return 'False'
											else: return 'False'
										elif obj[11]>4:
											return 'True'
										else: return 'True'
									elif obj[9]>2:
										# {"feature": "Education", "instances": 21, "metric_value": 0.4537, "depth": 10}
										if obj[11]>0:
											return 'False'
										elif obj[11]<=0:
											# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[12]>18:
													return 'False'
												elif obj[12]<=18:
													# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]<=2:
														return 'False'
													elif obj[8]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[18]>2.0:
									# {"feature": "Age", "instances": 11, "metric_value": 0.684, "depth": 9}
									if obj[8]>2:
										return 'True'
									elif obj[8]<=2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]<=0:
											return 'False'
										elif obj[7]>0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[13]>6:
								# {"feature": "Coupon_validity", "instances": 35, "metric_value": 0.5917, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Maritalstatus", "instances": 24, "metric_value": 0.7383, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Occupation", "instances": 23, "metric_value": 0.6666, "depth": 10}
										if obj[12]>6:
											# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 11}
											if obj[8]>0:
												# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 12}
												if obj[11]>1:
													# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[15]>0.0:
														# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[0]>1:
															return 'False'
														elif obj[0]<=1:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]>0:
																return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[15]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[11]<=1:
													return 'False'
												else: return 'False'
											elif obj[8]<=0:
												return 'True'
											else: return 'True'
										elif obj[12]<=6:
											return 'False'
										else: return 'False'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]<=30:
							# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.6098, "depth": 7}
							if obj[18]<=1.0:
								# {"feature": "Age", "instances": 27, "metric_value": 0.7642, "depth": 8}
								if obj[8]<=3:
									# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 9}
									if obj[12]<=9:
										# {"feature": "Coupon_validity", "instances": 14, "metric_value": 0.9852, "depth": 10}
										if obj[6]>0:
											# {"feature": "Gender", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[7]>0:
												return 'False'
											elif obj[7]<=0:
												# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[1]>0:
													# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[15]>0.0:
														return 'False'
													elif obj[15]<=0.0:
														return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[12]>9:
										return 'False'
									else: return 'False'
								elif obj[8]>3:
									return 'False'
								else: return 'False'
							elif obj[18]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>3:
						# {"feature": "Carryaway", "instances": 47, "metric_value": 0.551, "depth": 6}
						if obj[16]<=2.0:
							# {"feature": "Passanger", "instances": 27, "metric_value": 0.7642, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Occupation", "instances": 25, "metric_value": 0.6343, "depth": 8}
								if obj[12]>1:
									# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.4395, "depth": 9}
									if obj[15]<=1.0:
										return 'False'
									elif obj[15]>1.0:
										# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[11]<=0:
											return 'False'
										elif obj[11]>0:
											# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[13]>3:
												return 'True'
											elif obj[13]<=3:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[12]<=1:
									# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[17]>1.0:
										return 'True'
									elif obj[17]<=1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								return 'True'
							else: return 'True'
						elif obj[16]>2.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[2]>0:
					# {"feature": "Passanger", "instances": 142, "metric_value": 0.6554, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Education", "instances": 126, "metric_value": 0.5917, "depth": 6}
						if obj[11]>0:
							# {"feature": "Temperature", "instances": 92, "metric_value": 0.4621, "depth": 7}
							if obj[3]<=30:
								# {"feature": "Coffeehouse", "instances": 53, "metric_value": 0.6122, "depth": 8}
								if obj[15]<=2.0:
									# {"feature": "Occupation", "instances": 39, "metric_value": 0.7321, "depth": 9}
									if obj[12]<=11:
										# {"feature": "Age", "instances": 28, "metric_value": 0.5917, "depth": 10}
										if obj[8]<=3:
											# {"feature": "Income", "instances": 16, "metric_value": 0.8113, "depth": 11}
											if obj[13]>1:
												# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.6194, "depth": 12}
												if obj[17]<=2.0:
													# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[4]>0:
														# {"feature": "Carryaway", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[16]<=2.0:
															return 'False'
														elif obj[16]>2.0:
															# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9]<=0:
																return 'True'
															elif obj[9]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[17]>2.0:
													return 'False'
												else: return 'False'
											elif obj[13]<=1:
												# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[0]<=1:
													return 'True'
												elif obj[0]>1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>3:
											return 'False'
										else: return 'False'
									elif obj[12]>11:
										# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[20]>1:
													# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8]>3:
														# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[0]>0:
															return 'True'
														elif obj[0]<=0:
															return 'False'
														else: return 'False'
													elif obj[8]<=3:
														return 'False'
													else: return 'False'
												elif obj[20]<=1:
													return 'True'
												else: return 'True'
											elif obj[4]>1:
												return 'False'
											else: return 'False'
										elif obj[17]<=1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[15]>2.0:
									return 'False'
								else: return 'False'
							elif obj[3]>30:
								# {"feature": "Income", "instances": 39, "metric_value": 0.172, "depth": 8}
								if obj[13]<=7:
									return 'False'
								elif obj[13]>7:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[11]<=0:
							# {"feature": "Age", "instances": 34, "metric_value": 0.8338, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Driving_to", "instances": 19, "metric_value": 0.4855, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[9]<=0:
										# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[16]<=2.0:
											return 'False'
										elif obj[16]>2.0:
											return 'True'
										else: return 'True'
									elif obj[9]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>2:
								# {"feature": "Income", "instances": 15, "metric_value": 0.9968, "depth": 8}
								if obj[13]>3:
									# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[6]<=0:
										# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[17]>-1.0:
											return 'False'
										elif obj[17]<=-1.0:
											# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0]<=1:
												return 'True'
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[6]>0:
										return 'True'
									else: return 'True'
								elif obj[13]<=3:
									# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[12]>4:
										return 'True'
									elif obj[12]<=4:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[11]<=2:
							# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[13]<=3:
								return 'False'
							elif obj[13]>3:
								# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[12]<=19:
									return 'True'
								elif obj[12]>19:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[14]>1.0:
			# {"feature": "Direction_same", "instances": 401, "metric_value": 0.9689, "depth": 3}
			if obj[19]<=0:
				# {"feature": "Restaurant20to50", "instances": 313, "metric_value": 0.991, "depth": 4}
				if obj[18]<=2.0:
					# {"feature": "Driving_to", "instances": 262, "metric_value": 0.9989, "depth": 5}
					if obj[0]<=0:
						# {"feature": "Age", "instances": 133, "metric_value": 0.9654, "depth": 6}
						if obj[8]>1:
							# {"feature": "Restaurantlessthan20", "instances": 80, "metric_value": 0.9995, "depth": 7}
							if obj[17]<=3.0:
								# {"feature": "Time", "instances": 75, "metric_value": 0.9937, "depth": 8}
								if obj[4]>0:
									# {"feature": "Children", "instances": 66, "metric_value": 1.0, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Income", "instances": 45, "metric_value": 0.9825, "depth": 10}
										if obj[13]>0:
											# {"feature": "Coupon_validity", "instances": 40, "metric_value": 0.9982, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Occupation", "instances": 28, "metric_value": 0.9059, "depth": 12}
												if obj[12]<=9:
													# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9427, "depth": 13}
													if obj[15]>1.0:
														# {"feature": "Passanger", "instances": 18, "metric_value": 0.8524, "depth": 14}
														if obj[1]>0:
															# {"feature": "Carryaway", "instances": 13, "metric_value": 0.9612, "depth": 15}
															if obj[16]>2.0:
																# {"feature": "Education", "instances": 11, "metric_value": 0.994, "depth": 16}
																if obj[11]<=1:
																	# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 17}
																	if obj[2]>0:
																		# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[9]>1:
																			return 'False'
																		elif obj[9]<=1:
																			return 'True'
																		else: return 'True'
																	elif obj[2]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[11]>1:
																	# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[9]<=1:
																		return 'False'
																	elif obj[9]>1:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[16]<=2.0:
																return 'True'
															else: return 'True'
														elif obj[1]<=0:
															return 'True'
														else: return 'True'
													elif obj[15]<=1.0:
														# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[11]>0:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=3:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=2.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[11]<=0:
																	return 'False'
																else: return 'False'
															elif obj[7]>0:
																return 'True'
															else: return 'True'
														elif obj[9]>1:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[12]>9:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[11]<=3:
													# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 13}
													if obj[12]<=16:
														return 'False'
													elif obj[12]>16:
														return 'True'
													else: return 'True'
												elif obj[11]>3:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[13]<=0:
											return 'True'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.9183, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 11}
											if obj[1]>0:
												# {"feature": "Carryaway", "instances": 14, "metric_value": 0.5917, "depth": 12}
												if obj[16]>2.0:
													# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[15]<=2.0:
														# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[12]>6:
															# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[2]>0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]<=0:
																	return 'False'
																elif obj[7]>0:
																	return 'True'
																else: return 'True'
															elif obj[2]<=0:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]<=0:
																	return 'True'
																elif obj[7]>0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[12]<=6:
															return 'False'
														else: return 'False'
													elif obj[15]>2.0:
														return 'False'
													else: return 'False'
												elif obj[16]<=2.0:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[9]>1:
											# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[12]>1:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[20]>1:
													return 'True'
												elif obj[20]<=1:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=1:
														return 'True'
													elif obj[1]>1:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[4]<=0:
									# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[12]<=14:
										return 'True'
									elif obj[12]>14:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[17]>3.0:
								return 'False'
							else: return 'False'
						elif obj[8]<=1:
							# {"feature": "Temperature", "instances": 53, "metric_value": 0.8037, "depth": 7}
							if obj[3]>30:
								# {"feature": "Income", "instances": 44, "metric_value": 0.6321, "depth": 8}
								if obj[13]>3:
									# {"feature": "Carryaway", "instances": 24, "metric_value": 0.2499, "depth": 9}
									if obj[16]>1.0:
										return 'True'
									elif obj[16]<=1.0:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]>1:
											return 'True'
										elif obj[1]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]<=3:
									# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.5436, "depth": 10}
										if obj[15]>0.0:
											return 'True'
										elif obj[15]<=0.0:
											# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[4]>2:
												# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[2]>0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[12]<=1:
														return 'False'
													elif obj[12]>1:
														return 'True'
													else: return 'True'
												elif obj[2]<=0:
													return 'True'
												else: return 'True'
											elif obj[4]<=2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[3]<=30:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Carryaway", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[16]<=2.0:
										# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[2]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]>0:
												return 'True'
											elif obj[7]<=0:
												return 'False'
											else: return 'False'
										elif obj[2]<=0:
											return 'False'
										else: return 'False'
									elif obj[16]>2.0:
										return 'True'
									else: return 'True'
								elif obj[11]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]>0:
						# {"feature": "Coupon_validity", "instances": 129, "metric_value": 0.9843, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Age", "instances": 109, "metric_value": 0.9999, "depth": 7}
							if obj[8]<=5:
								# {"feature": "Time", "instances": 98, "metric_value": 0.9925, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Distance", "instances": 79, "metric_value": 0.9999, "depth": 9}
									if obj[20]>1:
										# {"feature": "Restaurantlessthan20", "instances": 76, "metric_value": 0.9995, "depth": 10}
										if obj[17]<=3.0:
											# {"feature": "Gender", "instances": 74, "metric_value": 0.9979, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Income", "instances": 46, "metric_value": 0.9781, "depth": 12}
												if obj[13]>0:
													# {"feature": "Coffeehouse", "instances": 42, "metric_value": 0.9934, "depth": 13}
													if obj[15]>0.0:
														# {"feature": "Carryaway", "instances": 36, "metric_value": 0.9641, "depth": 14}
														if obj[16]>1.0:
															# {"feature": "Occupation", "instances": 30, "metric_value": 0.9871, "depth": 15}
															if obj[12]>1:
																# {"feature": "Education", "instances": 28, "metric_value": 0.9666, "depth": 16}
																if obj[11]<=2:
																	# {"feature": "Maritalstatus", "instances": 27, "metric_value": 0.951, "depth": 17}
																	if obj[9]>0:
																		# {"feature": "Children", "instances": 24, "metric_value": 0.9799, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Temperature", "instances": 23, "metric_value": 0.9656, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Weather", "instances": 19, "metric_value": 0.9495, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 21}
																					if obj[1]<=1:
																						return 'True'
																					else: return 'True'
																				elif obj[2]>0:
																					# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 21}
																					if obj[1]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[3]>55:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[9]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[11]>2:
																	return 'False'
																else: return 'False'
															elif obj[12]<=1:
																return 'False'
															else: return 'False'
														elif obj[16]<=1.0:
															# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[11]<=0:
																# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[12]<=1:
																		return 'True'
																	elif obj[12]>1:
																		return 'False'
																	else: return 'False'
																elif obj[2]>0:
																	return 'True'
																else: return 'True'
															elif obj[11]>0:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[15]<=0.0:
														# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[3]<=55:
															return 'False'
														elif obj[3]>55:
															# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12]>6:
																return 'True'
															elif obj[12]<=6:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'False'
												elif obj[13]<=0:
													return 'True'
												else: return 'True'
											elif obj[7]>0:
												# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 12}
												if obj[11]>0:
													# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.8366, "depth": 13}
													if obj[15]<=1.0:
														# {"feature": "Children", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[12]>1:
																# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=55:
																			# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[9]>0:
																				# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[13]<=2:
																					# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[16]<=3.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[9]<=0:
																				# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[13]<=5:
																					# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[16]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[12]<=1:
																return 'True'
															else: return 'True'
														elif obj[10]>0:
															return 'False'
														else: return 'False'
													elif obj[15]>1.0:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													# {"feature": "Occupation", "instances": 13, "metric_value": 0.9612, "depth": 13}
													if obj[12]>2:
														# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.8454, "depth": 14}
														if obj[15]>0.0:
															# {"feature": "Weather", "instances": 10, "metric_value": 0.7219, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[13]>2:
																	# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Carryaway", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[16]>2.0:
																						return 'False'
																					elif obj[16]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[3]>55:
																		return 'True'
																	else: return 'True'
																elif obj[13]<=2:
																	return 'True'
																else: return 'True'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														elif obj[15]<=0.0:
															return 'False'
														else: return 'False'
													elif obj[12]<=2:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[17]>3.0:
											return 'False'
										else: return 'False'
									elif obj[20]<=1:
										return 'False'
									else: return 'False'
								elif obj[4]>1:
									# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.8315, "depth": 9}
									if obj[17]<=2.0:
										return 'False'
									elif obj[17]>2.0:
										# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[15]<=1.0:
											# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[12]>1:
												return 'False'
											elif obj[12]<=1:
												return 'True'
											else: return 'True'
										elif obj[15]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>5:
								# {"feature": "Temperature", "instances": 11, "metric_value": 0.4395, "depth": 8}
								if obj[3]<=55:
									return 'True'
								elif obj[3]>55:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]>1:
										return 'True'
									elif obj[4]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Income", "instances": 20, "metric_value": 0.2864, "depth": 7}
							if obj[13]>0:
								return 'False'
							elif obj[13]<=0:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2]>0:
									return 'False'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[18]>2.0:
					# {"feature": "Age", "instances": 51, "metric_value": 0.819, "depth": 5}
					if obj[8]>0:
						# {"feature": "Carryaway", "instances": 39, "metric_value": 0.6194, "depth": 6}
						if obj[16]>2.0:
							# {"feature": "Coupon_validity", "instances": 21, "metric_value": 0.2762, "depth": 7}
							if obj[6]<=0:
								return 'True'
							elif obj[6]>0:
								# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]<=0:
									return 'True'
								elif obj[2]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[16]<=2.0:
							# {"feature": "Income", "instances": 18, "metric_value": 0.8524, "depth": 7}
							if obj[13]>1:
								# {"feature": "Temperature", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[3]<=55:
									# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[2]<=1:
											# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[11]<=2:
												return 'False'
											elif obj[11]>2:
												return 'True'
											else: return 'True'
										elif obj[2]>1:
											return 'True'
										else: return 'True'
									elif obj[1]>2:
										return 'True'
									else: return 'True'
								elif obj[3]>55:
									return 'False'
								else: return 'False'
							elif obj[13]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]<=0:
						# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 6}
						if obj[12]>9:
							# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[13]<=6:
								return 'False'
							elif obj[13]>6:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=0:
									return 'False'
								elif obj[1]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[12]<=9:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[19]>0:
				# {"feature": "Coupon_validity", "instances": 88, "metric_value": 0.7732, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Age", "instances": 63, "metric_value": 0.5491, "depth": 5}
					if obj[8]>1:
						# {"feature": "Occupation", "instances": 38, "metric_value": 0.7425, "depth": 6}
						if obj[12]<=10:
							# {"feature": "Children", "instances": 26, "metric_value": 0.8905, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9457, "depth": 8}
								if obj[18]<=1.0:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 1.0, "depth": 9}
									if obj[15]<=2.0:
										# {"feature": "Carryaway", "instances": 8, "metric_value": 0.9544, "depth": 10}
										if obj[16]>2.0:
											# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[7]>0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=1:
													return 'True'
												elif obj[11]>1:
													return 'False'
												else: return 'False'
											elif obj[7]<=0:
												return 'False'
											else: return 'False'
										elif obj[16]<=2.0:
											return 'True'
										else: return 'True'
									elif obj[15]>2.0:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]<=55:
											return 'False'
										elif obj[3]>55:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[18]>1.0:
									# {"feature": "Income", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[13]>0:
										# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[11]>0:
											return 'True'
										elif obj[11]<=0:
											# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[3]>55:
												# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[4]<=0:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]>0:
														return 'True'
													elif obj[7]<=0:
														return 'False'
													else: return 'False'
												elif obj[4]>0:
													return 'True'
												else: return 'True'
											elif obj[3]<=55:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[13]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[10]>0:
								return 'True'
							else: return 'True'
						elif obj[12]>10:
							return 'True'
						else: return 'True'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				elif obj[6]>0:
					# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9988, "depth": 5}
					if obj[15]>0.0:
						# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.994, "depth": 6}
						if obj[18]>0.0:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 7}
							if obj[12]<=16:
								# {"feature": "Carryaway", "instances": 17, "metric_value": 0.9975, "depth": 8}
								if obj[16]<=3.0:
									# {"feature": "Income", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[13]>0:
										# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Driving_to", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[9]<=1:
													# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[17]>1.0:
														return 'True'
													elif obj[17]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[9]>1:
													return 'False'
												else: return 'False'
											elif obj[0]>1:
												return 'True'
											else: return 'True'
										elif obj[11]>2:
											return 'False'
										else: return 'False'
									elif obj[13]<=0:
										# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[11]<=2:
											return 'False'
										elif obj[11]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[16]>3.0:
									return 'False'
								else: return 'False'
							elif obj[12]>16:
								return 'True'
							else: return 'True'
						elif obj[18]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[15]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
