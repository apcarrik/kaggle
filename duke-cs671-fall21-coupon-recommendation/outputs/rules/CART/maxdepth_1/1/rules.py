def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 5092, "metric_value": 0.988, "depth": 1}
	if obj[5]>1:
		# {"feature": "Coupon_validity", "instances": 3670, "metric_value": 0.9556, "depth": 2}
		if obj[6]>0:
			# {"feature": "Driving_to", "instances": 1888, "metric_value": 0.9971, "depth": 3}
			if obj[0]<=0:
				# {"feature": "Coffeehouse", "instances": 997, "metric_value": 0.946, "depth": 4}
				if obj[15]<=1.0:
					# {"feature": "Occupation", "instances": 514, "metric_value": 0.9866, "depth": 5}
					if obj[12]<=8.060311284046692:
						# {"feature": "Restaurant20to50", "instances": 312, "metric_value": 0.9496, "depth": 6}
						if obj[18]<=1.0:
							# {"feature": "Time", "instances": 234, "metric_value": 0.9743, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Distance", "instances": 118, "metric_value": 0.9992, "depth": 8}
								if obj[20]>1:
									# {"feature": "Carryaway", "instances": 72, "metric_value": 0.9641, "depth": 9}
									if obj[16]<=2.0:
										# {"feature": "Gender", "instances": 43, "metric_value": 0.8841, "depth": 10}
										if obj[7]>0:
											# {"feature": "Passanger", "instances": 24, "metric_value": 0.9799, "depth": 11}
											if obj[1]>2:
												# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 12}
												if obj[11]<=2:
													# {"feature": "Income", "instances": 15, "metric_value": 0.7219, "depth": 13}
													if obj[13]<=6:
														# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 14}
														if obj[10]>0:
															# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[8]>1:
																# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[14]<=0.0:
																	# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=0:
																				# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[17]>1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[14]>0.0:
																	return 'True'
																else: return 'True'
															elif obj[8]<=1:
																return 'True'
															else: return 'True'
														elif obj[10]<=0:
															return 'True'
														else: return 'True'
													elif obj[13]>6:
														return 'False'
													else: return 'False'
												elif obj[11]>2:
													# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[13]<=1:
														return 'False'
													elif obj[13]>1:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=80:
																# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[8]<=1:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=4.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=1.0:
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
												# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[2]<=1:
													return 'False'
												elif obj[2]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[7]<=0:
											# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.6292, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Age", "instances": 15, "metric_value": 0.3534, "depth": 12}
												if obj[8]>0:
													return 'True'
												elif obj[8]<=0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=3:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=80:
																# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[11]<=4:
																		# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[13]<=4:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=1.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=1.0:
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
											elif obj[9]>1:
												# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[13]>3:
													# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=2:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=3:
															# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=80:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=0.0:
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
													elif obj[8]>2:
														return 'True'
													else: return 'True'
												elif obj[13]<=3:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[16]>2.0:
										# {"feature": "Restaurantlessthan20", "instances": 29, "metric_value": 0.9991, "depth": 10}
										if obj[17]>-1.0:
											# {"feature": "Age", "instances": 27, "metric_value": 0.9911, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Income", "instances": 22, "metric_value": 0.9457, "depth": 12}
												if obj[13]<=3:
													# {"feature": "Weather", "instances": 14, "metric_value": 1.0, "depth": 13}
													if obj[2]<=1:
														# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 14}
														if obj[11]<=3:
															# {"feature": "Passanger", "instances": 12, "metric_value": 1.0, "depth": 15}
															if obj[1]>0:
																# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9911, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 17}
																	if obj[3]>55:
																		# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[14]>0.0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[14]<=0.0:
																				return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[3]<=55:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[9]>1:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[1]<=0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[7]<=0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[11]>3:
															return 'True'
														else: return 'True'
													elif obj[2]>1:
														return 'False'
													else: return 'False'
												elif obj[13]>3:
													# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[2]<=0:
														return 'False'
													elif obj[2]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]>4:
												# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[9]<=1:
													return 'True'
												elif obj[9]>1:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=2:
														return 'False'
													elif obj[1]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[17]<=-1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[20]<=1:
									# {"feature": "Income", "instances": 46, "metric_value": 0.9503, "depth": 9}
									if obj[13]>0:
										# {"feature": "Restaurantlessthan20", "instances": 41, "metric_value": 0.9012, "depth": 10}
										if obj[17]>0.0:
											# {"feature": "Age", "instances": 35, "metric_value": 0.8224, "depth": 11}
											if obj[8]>1:
												# {"feature": "Bar", "instances": 25, "metric_value": 0.7219, "depth": 12}
												if obj[14]<=0.0:
													# {"feature": "Gender", "instances": 14, "metric_value": 0.3712, "depth": 13}
													if obj[7]<=0:
														return 'False'
													elif obj[7]>0:
														# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[3]>55:
															return 'False'
														elif obj[3]<=55:
															# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[16]>1.0:
																return 'False'
															elif obj[16]<=1.0:
																return 'True'
															else: return 'True'
														else: return 'False'
													else: return 'False'
												elif obj[14]>0.0:
													# {"feature": "Gender", "instances": 11, "metric_value": 0.9457, "depth": 13}
													if obj[7]>0:
														# {"feature": "Carryaway", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[16]<=3.0:
															return 'False'
														elif obj[16]>3.0:
															# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[1]<=1:
																return 'False'
															elif obj[1]>1:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[7]<=0:
														# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9]>1:
															# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[11]>0:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=0:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=3.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[11]<=0:
																return 'False'
															else: return 'False'
														elif obj[9]<=1:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]<=1:
												# {"feature": "Carryaway", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[16]>2.0:
													# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[11]<=3:
														return 'False'
													elif obj[11]>3:
														return 'True'
													else: return 'True'
												elif obj[16]<=2.0:
													# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[1]<=0:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7]<=0:
															return 'False'
														elif obj[7]>0:
															return 'True'
														else: return 'True'
													elif obj[1]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[17]<=0.0:
											# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=55:
												return 'True'
											elif obj[3]>55:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]>0:
													return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[13]<=0:
										# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[11]<=1:
											return 'True'
										elif obj[11]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[4]>2:
								# {"feature": "Gender", "instances": 116, "metric_value": 0.9124, "depth": 8}
								if obj[7]>0:
									# {"feature": "Bar", "instances": 65, "metric_value": 0.8051, "depth": 9}
									if obj[14]>-1.0:
										# {"feature": "Restaurantlessthan20", "instances": 63, "metric_value": 0.7642, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Age", "instances": 36, "metric_value": 0.888, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Maritalstatus", "instances": 34, "metric_value": 0.8338, "depth": 12}
												if obj[9]<=2:
													# {"feature": "Income", "instances": 32, "metric_value": 0.7579, "depth": 13}
													if obj[13]<=4:
														# {"feature": "Education", "instances": 25, "metric_value": 0.8555, "depth": 14}
														if obj[11]<=2:
															# {"feature": "Carryaway", "instances": 23, "metric_value": 0.7554, "depth": 15}
															if obj[16]>1.0:
																# {"feature": "Passanger", "instances": 19, "metric_value": 0.6292, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Distance", "instances": 14, "metric_value": 0.3712, "depth": 17}
																	if obj[20]>1:
																		return 'True'
																	elif obj[20]<=1:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[10]<=0:
																			return 'True'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[1]<=1:
																	# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[20]<=1:
																		return 'True'
																	elif obj[20]>1:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[16]<=1.0:
																# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[20]>1:
																	# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[1]<=2:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[1]>2:
																		return 'True'
																	else: return 'True'
																elif obj[20]<=1:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[11]>2:
															return 'False'
														else: return 'False'
													elif obj[13]>4:
														return 'True'
													else: return 'True'
												elif obj[9]>2:
													return 'False'
												else: return 'False'
											elif obj[8]>4:
												return 'False'
											else: return 'False'
										elif obj[17]<=1.0:
											# {"feature": "Children", "instances": 27, "metric_value": 0.5033, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Carryaway", "instances": 14, "metric_value": 0.7496, "depth": 12}
												if obj[16]<=1.0:
													return 'True'
												elif obj[16]>1.0:
													# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[11]<=2:
														# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[13]>1:
															return 'False'
														elif obj[13]<=1:
															return 'True'
														else: return 'True'
													elif obj[11]>2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[14]<=-1.0:
										return 'False'
									else: return 'False'
								elif obj[7]<=0:
									# {"feature": "Age", "instances": 51, "metric_value": 0.9864, "depth": 9}
									if obj[8]>3:
										# {"feature": "Maritalstatus", "instances": 29, "metric_value": 0.9923, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Temperature", "instances": 26, "metric_value": 1.0, "depth": 11}
											if obj[3]>30:
												# {"feature": "Carryaway", "instances": 24, "metric_value": 0.995, "depth": 12}
												if obj[16]>0.0:
													# {"feature": "Bar", "instances": 22, "metric_value": 0.976, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 14}
														if obj[11]<=1:
															# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.994, "depth": 15}
															if obj[17]>1.0:
																# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[13]>0:
																		return 'True'
																	elif obj[13]<=0:
																		# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[20]<=1:
																			return 'False'
																		elif obj[20]>1:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																elif obj[1]<=1:
																	# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[20]>1:
																			return 'True'
																		elif obj[20]<=1:
																			return 'False'
																		else: return 'False'
																	elif obj[10]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[17]<=1.0:
																return 'False'
															else: return 'False'
														elif obj[11]>1:
															# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[13]<=1:
																return 'False'
															elif obj[13]>1:
																# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=1.0:
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
																elif obj[1]<=1:
																	return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[14]>1.0:
														# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[13]<=3:
															return 'True'
														elif obj[13]>3:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[16]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									elif obj[8]<=3:
										# {"feature": "Restaurantlessthan20", "instances": 22, "metric_value": 0.8454, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Temperature", "instances": 17, "metric_value": 0.6723, "depth": 11}
											if obj[3]>55:
												# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[13]>0:
													# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[20]>1:
														# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[9]<=1:
															# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[1]>1:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=1:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=0.0:
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
															elif obj[1]<=1:
																return 'False'
															else: return 'False'
														elif obj[9]>1:
															return 'True'
														else: return 'True'
													elif obj[20]<=1:
														return 'True'
													else: return 'True'
												elif obj[13]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=55:
												return 'True'
											else: return 'True'
										elif obj[17]<=1.0:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[1]<=0:
												# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9]>0:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[20]>1:
														return 'False'
													elif obj[20]<=1:
														return 'True'
													else: return 'True'
												elif obj[9]<=0:
													return 'True'
												else: return 'True'
											elif obj[1]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[18]>1.0:
							# {"feature": "Restaurantlessthan20", "instances": 78, "metric_value": 0.8213, "depth": 7}
							if obj[17]<=3.0:
								# {"feature": "Education", "instances": 73, "metric_value": 0.7587, "depth": 8}
								if obj[11]<=3:
									# {"feature": "Weather", "instances": 67, "metric_value": 0.793, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Distance", "instances": 66, "metric_value": 0.7732, "depth": 10}
										if obj[20]>1:
											# {"feature": "Time", "instances": 34, "metric_value": 0.6024, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												# {"feature": "Gender", "instances": 17, "metric_value": 0.874, "depth": 12}
												if obj[7]>0:
													# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[13]>1:
														# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[16]<=2.0:
															return 'True'
														elif obj[16]>2.0:
															return 'False'
														else: return 'False'
													elif obj[13]<=1:
														return 'False'
													else: return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[20]<=1:
											# {"feature": "Age", "instances": 32, "metric_value": 0.896, "depth": 11}
											if obj[8]>1:
												# {"feature": "Income", "instances": 19, "metric_value": 0.998, "depth": 12}
												if obj[13]>1:
													# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 13}
													if obj[4]>0:
														# {"feature": "Temperature", "instances": 10, "metric_value": 1.0, "depth": 14}
														if obj[3]>30:
															# {"feature": "Carryaway", "instances": 9, "metric_value": 0.9911, "depth": 15}
															if obj[16]>-1.0:
																# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.9544, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[14]>0.0:
																			return 'False'
																		elif obj[14]<=0.0:
																			return 'True'
																		else: return 'True'
																	elif obj[10]>0:
																		return 'True'
																	else: return 'True'
																elif obj[9]>1:
																	return 'True'
																else: return 'True'
															elif obj[16]<=-1.0:
																return 'False'
															else: return 'False'
														elif obj[3]<=30:
															return 'False'
														else: return 'False'
													elif obj[4]<=0:
														return 'False'
													else: return 'False'
												elif obj[13]<=1:
													# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[3]>30:
														return 'True'
													elif obj[3]<=30:
														# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[4]>3:
															return 'True'
														elif obj[4]<=3:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=1:
												# {"feature": "Children", "instances": 13, "metric_value": 0.3912, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1]>1:
														return 'True'
													elif obj[1]<=1:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[2]>1:
										return 'False'
									else: return 'False'
								elif obj[11]>3:
									return 'True'
								else: return 'True'
							elif obj[17]>3.0:
								# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[2]<=0:
									return 'False'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[12]>8.060311284046692:
						# {"feature": "Bar", "instances": 202, "metric_value": 0.9975, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Carryaway", "instances": 177, "metric_value": 0.9989, "depth": 7}
							if obj[16]<=3.0:
								# {"feature": "Income", "instances": 161, "metric_value": 0.9899, "depth": 8}
								if obj[13]<=6:
									# {"feature": "Restaurant20to50", "instances": 138, "metric_value": 0.9742, "depth": 9}
									if obj[18]>-1.0:
										# {"feature": "Education", "instances": 131, "metric_value": 0.9814, "depth": 10}
										if obj[11]>0:
											# {"feature": "Maritalstatus", "instances": 103, "metric_value": 0.9945, "depth": 11}
											if obj[9]<=0:
												# {"feature": "Time", "instances": 56, "metric_value": 0.9666, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Age", "instances": 31, "metric_value": 0.9932, "depth": 13}
													if obj[8]<=3:
														# {"feature": "Temperature", "instances": 25, "metric_value": 0.9427, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Restaurantlessthan20", "instances": 15, "metric_value": 0.7219, "depth": 15}
															if obj[17]<=3.0:
																# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 16}
																if obj[10]>0:
																	return 'False'
																elif obj[10]<=0:
																	# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[2]<=1:
																		# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[1]<=1:
																			return 'False'
																		elif obj[1]>1:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[2]>1:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[17]>3.0:
																return 'True'
															else: return 'True'
														elif obj[3]>55:
															# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 15}
															if obj[1]>2:
																# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 16}
																if obj[17]>1.0:
																	# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[20]>1:
																		# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[10]>0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]<=0:
																				return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[20]<=1:
																		return 'True'
																	else: return 'True'
																elif obj[17]<=1.0:
																	return 'True'
																else: return 'True'
															elif obj[1]<=2:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[8]>3:
														# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[1]>1:
															return 'True'
														elif obj[1]<=1:
															# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[20]<=1:
																return 'True'
															elif obj[20]>1:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[4]>3:
													# {"feature": "Age", "instances": 25, "metric_value": 0.7219, "depth": 13}
													if obj[8]<=2:
														# {"feature": "Temperature", "instances": 17, "metric_value": 0.5226, "depth": 14}
														if obj[3]>30:
															# {"feature": "Restaurantlessthan20", "instances": 15, "metric_value": 0.3534, "depth": 15}
															if obj[17]<=2.0:
																return 'True'
															elif obj[17]>2.0:
																# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[20]<=1:
																	return 'True'
																elif obj[20]>1:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=2:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=1:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
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
														elif obj[3]<=30:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[10]<=0:
																return 'False'
															elif obj[10]>0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[8]>2:
														# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[17]<=2.0:
															# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 15}
															if obj[7]>0:
																# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[20]>1:
																		# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[20]<=1:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=1:
																	return 'True'
																else: return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														elif obj[17]>2.0:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]>0:
												# {"feature": "Time", "instances": 47, "metric_value": 0.9971, "depth": 12}
												if obj[4]<=3:
													# {"feature": "Children", "instances": 27, "metric_value": 0.951, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Passanger", "instances": 15, "metric_value": 0.7219, "depth": 14}
														if obj[1]>0:
															# {"feature": "Age", "instances": 14, "metric_value": 0.5917, "depth": 15}
															if obj[8]>0:
																# {"feature": "Distance", "instances": 12, "metric_value": 0.4138, "depth": 16}
																if obj[20]>1:
																	return 'True'
																elif obj[20]<=1:
																	# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[3]<=55:
																		return 'True'
																	elif obj[3]>55:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[8]<=0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=1:
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
																else: return 'True'
															else: return 'True'
														elif obj[1]<=0:
															return 'False'
														else: return 'False'
													elif obj[10]>0:
														# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[1]>1:
															# {"feature": "Weather", "instances": 10, "metric_value": 0.8813, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 16}
																if obj[3]>55:
																	# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 17}
																	if obj[20]>1:
																		# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[17]>-1.0:
																				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[8]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[8]<=0:
																					return 'True'
																				else: return 'True'
																			elif obj[17]<=-1.0:
																				return 'False'
																			else: return 'False'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[20]<=1:
																		return 'False'
																	else: return 'False'
																elif obj[3]<=55:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														elif obj[1]<=1:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[4]>3:
													# {"feature": "Age", "instances": 20, "metric_value": 0.8113, "depth": 13}
													if obj[8]>0:
														# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.874, "depth": 14}
														if obj[17]<=2.0:
															# {"feature": "Children", "instances": 14, "metric_value": 0.9403, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Passanger", "instances": 11, "metric_value": 0.8454, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[7]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[1]<=1:
																	# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[3]>55:
																		# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[3]<=55:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[10]>0:
																# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[1]>1:
																	return 'True'
																elif obj[1]<=1:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[17]>2.0:
															return 'False'
														else: return 'False'
													elif obj[8]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[11]<=0:
											# {"feature": "Age", "instances": 28, "metric_value": 0.8631, "depth": 11}
											if obj[8]>1:
												# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.9457, "depth": 12}
												if obj[9]<=1:
													# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 13}
													if obj[1]>2:
														# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[17]>1.0:
															return 'True'
														elif obj[17]<=1.0:
															# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[4]>0:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
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
															elif obj[4]<=0:
																return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[1]<=2:
														return 'False'
													else: return 'False'
												elif obj[9]>1:
													# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[4]>2:
														# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[1]>0:
															# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[7]>0:
																# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[3]>30:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=2.0:
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
																elif obj[3]<=30:
																	return 'True'
																else: return 'True'
															elif obj[7]<=0:
																return 'False'
															else: return 'False'
														elif obj[1]<=0:
															return 'True'
														else: return 'True'
													elif obj[4]<=2:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[18]<=-1.0:
										# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[11]>0:
											return 'True'
										elif obj[11]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]>6:
									# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.9321, "depth": 9}
									if obj[17]<=2.0:
										# {"feature": "Passanger", "instances": 17, "metric_value": 0.6723, "depth": 10}
										if obj[1]>1:
											# {"feature": "Time", "instances": 14, "metric_value": 0.3712, "depth": 11}
											if obj[4]>0:
												return 'False'
											elif obj[4]<=0:
												# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[3]>55:
													# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]>2:
														return 'False'
													elif obj[8]<=2:
														return 'True'
													else: return 'True'
												elif obj[3]<=55:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[1]<=1:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4]<=2:
												return 'True'
											elif obj[4]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[17]>2.0:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[20]>1:
											return 'True'
										elif obj[20]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[16]>3.0:
								# {"feature": "Education", "instances": 16, "metric_value": 0.5436, "depth": 8}
								if obj[11]>0:
									# {"feature": "Income", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[13]>0:
										# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[3]>55:
											# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[1]>0:
												# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[4]>2:
													# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[20]<=1:
														return 'False'
													elif obj[20]>1:
														return 'True'
													else: return 'True'
												elif obj[4]<=2:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[4]<=0:
													return 'True'
												elif obj[4]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[3]<=55:
											return 'False'
										else: return 'False'
									elif obj[13]<=0:
										return 'False'
									else: return 'False'
								elif obj[11]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[14]>2.0:
							# {"feature": "Time", "instances": 25, "metric_value": 0.5294, "depth": 7}
							if obj[4]>2:
								return 'False'
							elif obj[4]<=2:
								# {"feature": "Children", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[10]<=0:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[10]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[15]>1.0:
					# {"feature": "Bar", "instances": 483, "metric_value": 0.8712, "depth": 5}
					if obj[14]<=3.0:
						# {"feature": "Occupation", "instances": 461, "metric_value": 0.8462, "depth": 6}
						if obj[12]<=17.69683060768701:
							# {"feature": "Maritalstatus", "instances": 432, "metric_value": 0.8649, "depth": 7}
							if obj[9]<=2:
								# {"feature": "Income", "instances": 416, "metric_value": 0.8472, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Education", "instances": 261, "metric_value": 0.7711, "depth": 9}
									if obj[11]<=3:
										# {"feature": "Restaurantlessthan20", "instances": 246, "metric_value": 0.7948, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Passanger", "instances": 234, "metric_value": 0.8146, "depth": 11}
											if obj[1]>2:
												# {"feature": "Carryaway", "instances": 148, "metric_value": 0.7137, "depth": 12}
												if obj[16]>0.0:
													# {"feature": "Restaurant20to50", "instances": 147, "metric_value": 0.7025, "depth": 13}
													if obj[18]>0.0:
														# {"feature": "Age", "instances": 129, "metric_value": 0.6589, "depth": 14}
														if obj[8]>2:
															# {"feature": "Distance", "instances": 69, "metric_value": 0.5176, "depth": 15}
															if obj[20]>1:
																# {"feature": "Children", "instances": 43, "metric_value": 0.6931, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Weather", "instances": 31, "metric_value": 0.7706, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Time", "instances": 30, "metric_value": 0.7838, "depth": 18}
																		if obj[4]<=2:
																			# {"feature": "Gender", "instances": 21, "metric_value": 0.7025, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Temperature", "instances": 13, "metric_value": 0.7793, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]>0:
																				# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 8, "metric_value": 0.5436, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[4]>2:
																			# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]>0:
																				# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[2]>0:
																		return 'True'
																	else: return 'True'
																elif obj[10]>0:
																	# {"feature": "Time", "instances": 12, "metric_value": 0.4138, "depth": 17}
																	if obj[4]>0:
																		# {"feature": "Gender", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[4]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[20]<=1:
																return 'True'
															else: return 'True'
														elif obj[8]<=2:
															# {"feature": "Temperature", "instances": 60, "metric_value": 0.7838, "depth": 15}
															if obj[3]>55:
																# {"feature": "Gender", "instances": 49, "metric_value": 0.73, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Time", "instances": 32, "metric_value": 0.6962, "depth": 17}
																	if obj[4]<=2:
																		# {"feature": "Children", "instances": 17, "metric_value": 0.7871, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Weather", "instances": 12, "metric_value": 0.8113, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 21}
																					if obj[20]>1:
																						return 'True'
																					elif obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[10]>0:
																			# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[4]>2:
																		# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 18}
																		if obj[20]>1:
																			# {"feature": "Children", "instances": 10, "metric_value": 0.7219, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[20]<=1:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[7]<=0:
																	# {"feature": "Time", "instances": 17, "metric_value": 0.7871, "depth": 17}
																	if obj[4]<=2:
																		# {"feature": "Children", "instances": 12, "metric_value": 0.65, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					elif obj[20]>1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[10]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[4]>2:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[3]<=55:
																# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 16}
																if obj[20]<=1:
																	# {"feature": "Gender", "instances": 10, "metric_value": 0.8813, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[4]<=2:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[4]>2:
																				return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[20]>1:
																	return 'False'
																else: return 'False'
															else: return 'True'
														else: return 'True'
													elif obj[18]<=0.0:
														# {"feature": "Age", "instances": 18, "metric_value": 0.9183, "depth": 14}
														if obj[8]<=4:
															# {"feature": "Time", "instances": 14, "metric_value": 0.9852, "depth": 15}
															if obj[4]<=2:
																# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 16}
																if obj[20]>1:
																	# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[10]<=0:
																			return 'False'
																		elif obj[10]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[20]<=1:
																	return 'False'
																else: return 'False'
															elif obj[4]>2:
																# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[3]<=55:
																		return 'True'
																	elif obj[3]>55:
																		return 'False'
																	else: return 'False'
																elif obj[10]>0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[8]>4:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[16]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[1]<=2:
												# {"feature": "Temperature", "instances": 86, "metric_value": 0.933, "depth": 12}
												if obj[3]>55:
													# {"feature": "Distance", "instances": 46, "metric_value": 0.7936, "depth": 13}
													if obj[20]>1:
														# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.971, "depth": 14}
														if obj[18]<=1.0:
															# {"feature": "Carryaway", "instances": 15, "metric_value": 0.971, "depth": 15}
															if obj[16]<=3.0:
																# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 16}
																if obj[8]<=1:
																	# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[4]>2:
																			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[4]<=2:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[8]>1:
																	# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[7]>0:
																		return 'False'
																	elif obj[7]<=0:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[4]<=4:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[16]>3.0:
																return 'True'
															else: return 'True'
														elif obj[18]>1.0:
															# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 15}
															if obj[8]>1:
																return 'True'
															elif obj[8]<=1:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[20]<=1:
														# {"feature": "Age", "instances": 21, "metric_value": 0.2762, "depth": 14}
														if obj[8]<=4:
															return 'True'
														elif obj[8]>4:
															# {"feature": "Carryaway", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[16]>2.0:
																return 'True'
															elif obj[16]<=2.0:
																# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[4]<=2:
																	return 'False'
																elif obj[4]>2:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[3]<=55:
													# {"feature": "Restaurant20to50", "instances": 40, "metric_value": 0.9982, "depth": 13}
													if obj[18]<=2.0:
														# {"feature": "Weather", "instances": 35, "metric_value": 0.9852, "depth": 14}
														if obj[2]<=1:
															# {"feature": "Gender", "instances": 31, "metric_value": 0.9629, "depth": 15}
															if obj[7]>0:
																# {"feature": "Carryaway", "instances": 19, "metric_value": 0.998, "depth": 16}
																if obj[16]<=3.0:
																	# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 17}
																	if obj[8]<=2:
																		# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 18}
																		if obj[20]<=1:
																			return 'True'
																		elif obj[20]>1:
																			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[4]<=0:
																				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[4]>0:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[8]>2:
																		# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[4]<=0:
																				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[20]>1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[20]<=1:
																					return 'False'
																				else: return 'False'
																			elif obj[4]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[10]<=0:
																			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[4]>0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[4]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[16]>3.0:
																	return 'False'
																else: return 'False'
															elif obj[7]<=0:
																# {"feature": "Time", "instances": 12, "metric_value": 0.8113, "depth": 16}
																if obj[4]>0:
																	# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 17}
																	if obj[8]<=4:
																		return 'True'
																	elif obj[8]>4:
																		# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[20]>1:
																			return 'True'
																		elif obj[20]<=1:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[4]<=0:
																	# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[10]>0:
																		return 'False'
																	elif obj[10]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'True'
														elif obj[2]>1:
															# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[8]>1:
																return 'False'
															elif obj[8]<=1:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[18]>2.0:
														# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[8]<=1:
															return 'False'
														elif obj[8]>1:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[17]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[11]>3:
										return 'True'
									else: return 'True'
								elif obj[13]>4:
									# {"feature": "Restaurant20to50", "instances": 155, "metric_value": 0.9383, "depth": 9}
									if obj[18]>0.0:
										# {"feature": "Age", "instances": 138, "metric_value": 0.9656, "depth": 10}
										if obj[8]<=6:
											# {"feature": "Education", "instances": 130, "metric_value": 0.9792, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Weather", "instances": 67, "metric_value": 0.8795, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Passanger", "instances": 61, "metric_value": 0.9127, "depth": 13}
													if obj[1]>1:
														# {"feature": "Carryaway", "instances": 40, "metric_value": 0.971, "depth": 14}
														if obj[16]>0.0:
															# {"feature": "Children", "instances": 38, "metric_value": 0.9495, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.9986, "depth": 16}
																if obj[17]>2.0:
																	# {"feature": "Distance", "instances": 15, "metric_value": 0.8366, "depth": 17}
																	if obj[20]<=1:
																		# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 18}
																		if obj[3]>30:
																			return 'True'
																		elif obj[3]<=30:
																			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[7]<=0:
																				return 'True'
																			elif obj[7]>0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[20]>1:
																		# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 18}
																		if obj[4]>0:
																			# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]>0:
																				# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[4]<=0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[17]<=2.0:
																	# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 17}
																	if obj[3]>30:
																		return 'False'
																	elif obj[3]<=30:
																		# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[4]<=3:
																			return 'True'
																		elif obj[4]>3:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																else: return 'False'
															elif obj[10]>0:
																# {"feature": "Time", "instances": 15, "metric_value": 0.7219, "depth": 16}
																if obj[4]<=2:
																	# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 17}
																	if obj[17]>2.0:
																		# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 18}
																		if obj[3]>55:
																			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[7]<=1:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[3]<=55:
																			return 'False'
																		else: return 'False'
																	elif obj[17]<=2.0:
																		return 'True'
																	else: return 'True'
																elif obj[4]>2:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[16]<=0.0:
															return 'False'
														else: return 'False'
													elif obj[1]<=1:
														# {"feature": "Temperature", "instances": 21, "metric_value": 0.7025, "depth": 14}
														if obj[3]>55:
															# {"feature": "Time", "instances": 17, "metric_value": 0.7871, "depth": 15}
															if obj[4]>2:
																# {"feature": "Carryaway", "instances": 15, "metric_value": 0.8366, "depth": 16}
																if obj[16]>0.0:
																	# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.8905, "depth": 17}
																	if obj[17]>1.0:
																		# {"feature": "Children", "instances": 12, "metric_value": 0.9183, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[20]>1:
																					return 'True'
																				elif obj[20]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[7]>0:
																				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[20]>1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[20]<=1:
																					return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[10]>0:
																			# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[20]>1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[20]<=1:
																					return 'True'
																				else: return 'True'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[17]<=1.0:
																		return 'True'
																	else: return 'True'
																elif obj[16]<=0.0:
																	return 'True'
																else: return 'True'
															elif obj[4]<=2:
																return 'True'
															else: return 'True'
														elif obj[3]<=55:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[2]>0:
													return 'True'
												else: return 'True'
											elif obj[11]>1:
												# {"feature": "Carryaway", "instances": 63, "metric_value": 0.9955, "depth": 12}
												if obj[16]<=3.0:
													# {"feature": "Gender", "instances": 55, "metric_value": 0.971, "depth": 13}
													if obj[7]>0:
														# {"feature": "Weather", "instances": 30, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Distance", "instances": 28, "metric_value": 0.9963, "depth": 15}
															if obj[20]>1:
																# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.9183, "depth": 16}
																if obj[17]>2.0:
																	# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 17}
																	if obj[4]>0:
																		return 'False'
																	elif obj[4]<=0:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]>2:
																			return 'True'
																		elif obj[1]<=2:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[17]<=2.0:
																	# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 17}
																	if obj[1]>1:
																		# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[3]>55:
																				# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[4]>2:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[4]<=2:
																					return 'True'
																				else: return 'True'
																			elif obj[3]<=55:
																				return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[1]<=1:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[20]<=1:
																# {"feature": "Temperature", "instances": 10, "metric_value": 0.8813, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[4]>0:
																		# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[1]>1:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				return 'False'
																			elif obj[10]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[1]<=1:
																			return 'True'
																		else: return 'True'
																	elif obj[4]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[3]>55:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'True'
														else: return 'True'
													elif obj[7]<=0:
														# {"feature": "Time", "instances": 25, "metric_value": 0.8555, "depth": 14}
														if obj[4]>0:
															# {"feature": "Passanger", "instances": 19, "metric_value": 0.7425, "depth": 15}
															if obj[1]>2:
																# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.8905, "depth": 16}
																if obj[17]>1.0:
																	# {"feature": "Children", "instances": 12, "metric_value": 0.9183, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 18}
																		if obj[3]>55:
																			# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[20]>1:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[20]<=1:
																				return 'True'
																			else: return 'True'
																		elif obj[3]<=55:
																			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[10]>0:
																		# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[20]<=1:
																			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[3]>30:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[3]<=30:
																				return 'False'
																			else: return 'False'
																		elif obj[20]>1:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[17]<=1.0:
																	return 'False'
																else: return 'False'
															elif obj[1]<=2:
																return 'False'
															else: return 'False'
														elif obj[4]<=0:
															# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 15}
															if obj[1]>2:
																# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[10]<=0:
																	return 'False'
																elif obj[10]>0:
																	return 'True'
																else: return 'True'
															elif obj[1]<=2:
																return 'True'
															else: return 'True'
														else: return 'False'
													else: return 'False'
												elif obj[16]>3.0:
													# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[4]<=2:
														return 'True'
													elif obj[4]>2:
														# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]>55:
															return 'False'
														elif obj[3]<=55:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[8]>6:
											return 'True'
										else: return 'True'
									elif obj[18]<=0.0:
										# {"feature": "Carryaway", "instances": 17, "metric_value": 0.3228, "depth": 10}
										if obj[16]>1.0:
											return 'True'
										elif obj[16]<=1.0:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4]<=0:
												return 'True'
											elif obj[4]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[9]>2:
								# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 8}
								if obj[4]>0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[20]>1:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[7]>0:
											# {"feature": "Carryaway", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[16]>3.0:
												# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[1]>2:
													return 'True'
												elif obj[1]<=2:
													return 'False'
												else: return 'False'
											elif obj[16]<=3.0:
												return 'False'
											else: return 'False'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									elif obj[20]<=1:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]<=55:
											# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1]<=1:
												return 'True'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										elif obj[3]>55:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[12]>17.69683060768701:
							# {"feature": "Temperature", "instances": 29, "metric_value": 0.3621, "depth": 7}
							if obj[3]>30:
								# {"feature": "Income", "instances": 28, "metric_value": 0.2223, "depth": 8}
								if obj[13]>0:
									return 'True'
								elif obj[13]<=0:
									# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[4]>2:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1]>0:
											# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[20]>1:
													return 'False'
												elif obj[20]<=1:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=30:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]>3.0:
						# {"feature": "Occupation", "instances": 22, "metric_value": 0.9024, "depth": 6}
						if obj[12]>2:
							# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Carryaway", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[16]<=3.0:
									# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[17]>1.0:
										return 'True'
									elif obj[17]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[16]>3.0:
									return 'False'
								else: return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						elif obj[12]<=2:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[0]>0:
				# {"feature": "Direction_same", "instances": 891, "metric_value": 0.9792, "depth": 4}
				if obj[19]<=0:
					# {"feature": "Passanger", "instances": 452, "metric_value": 0.8445, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coffeehouse", "instances": 440, "metric_value": 0.8184, "depth": 6}
						if obj[15]>1.0:
							# {"feature": "Occupation", "instances": 224, "metric_value": 0.9325, "depth": 7}
							if obj[12]>0:
								# {"feature": "Distance", "instances": 219, "metric_value": 0.9228, "depth": 8}
								if obj[20]>1:
									# {"feature": "Income", "instances": 179, "metric_value": 0.8964, "depth": 9}
									if obj[13]>2:
										# {"feature": "Restaurantlessthan20", "instances": 119, "metric_value": 0.9438, "depth": 10}
										if obj[17]<=3.0:
											# {"feature": "Age", "instances": 105, "metric_value": 0.9085, "depth": 11}
											if obj[8]>0:
												# {"feature": "Time", "instances": 84, "metric_value": 0.8469, "depth": 12}
												if obj[4]<=1:
													# {"feature": "Carryaway", "instances": 62, "metric_value": 0.9383, "depth": 13}
													if obj[16]<=2.0:
														# {"feature": "Bar", "instances": 32, "metric_value": 0.9972, "depth": 14}
														if obj[14]<=3.0:
															# {"feature": "Education", "instances": 30, "metric_value": 0.9871, "depth": 15}
															if obj[11]<=1:
																# {"feature": "Weather", "instances": 16, "metric_value": 0.9887, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 17}
																	if obj[10]<=0:
																		return 'False'
																	elif obj[10]>0:
																		# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[9]<=0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[2]>0:
																	# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 17}
																	if obj[18]<=2.0:
																		return 'True'
																	elif obj[18]>2.0:
																		# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[9]<=0:
																			return 'False'
																		elif obj[9]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																else: return 'True'
															elif obj[11]>1:
																# {"feature": "Temperature", "instances": 14, "metric_value": 0.8631, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.7793, "depth": 17}
																	if obj[9]<=2:
																		# {"feature": "Gender", "instances": 12, "metric_value": 0.65, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 19}
																			if obj[10]>0:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[2]<=1:
																					return 'False'
																				elif obj[2]>1:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=2.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[10]<=0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]>0:
																					return 'False'
																				elif obj[2]<=0:
																					return 'True'
																				else: return 'True'
																			else: return 'False'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[9]>2:
																		return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[14]>3.0:
															return 'True'
														else: return 'True'
													elif obj[16]>2.0:
														# {"feature": "Children", "instances": 30, "metric_value": 0.7838, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.9183, "depth": 15}
															if obj[9]>0:
																# {"feature": "Bar", "instances": 16, "metric_value": 0.8113, "depth": 16}
																if obj[14]>1.0:
																	# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[11]>0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]>1.0:
																						return 'False'
																					elif obj[18]<=1.0:
																						return 'True'
																					else: return 'True'
																				elif obj[11]<=0:
																					return 'True'
																				else: return 'True'
																			elif obj[2]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[11]>0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					return 'True'
																				elif obj[2]>0:
																					return 'False'
																				else: return 'False'
																			elif obj[11]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[3]>55:
																		return 'False'
																	else: return 'False'
																elif obj[14]<=1.0:
																	return 'False'
																else: return 'False'
															elif obj[9]<=0:
																return 'True'
															else: return 'True'
														elif obj[10]>0:
															# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 15}
															if obj[14]>0.0:
																return 'False'
															elif obj[14]<=0.0:
																# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[11]>0:
																	return 'False'
																elif obj[11]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[4]>1:
													# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.2668, "depth": 13}
													if obj[18]<=2.0:
														return 'False'
													elif obj[18]>2.0:
														# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9]<=1:
															return 'False'
														elif obj[9]>1:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=0:
												# {"feature": "Bar", "instances": 21, "metric_value": 0.9984, "depth": 12}
												if obj[14]>0.0:
													# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9403, "depth": 13}
													if obj[18]<=2.0:
														# {"feature": "Carryaway", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[16]>1.0:
															# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[10]<=0:
																		return 'False'
																	elif obj[10]>0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=0:
																			return 'False'
																		elif obj[11]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'False'
																elif obj[2]>0:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=30:
																		# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[4]<=3:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[11]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[9]>1:
																return 'False'
															else: return 'False'
														elif obj[16]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[18]>2.0:
														# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[2]>0:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=0:
																return 'True'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[2]<=0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[14]<=0.0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[7]>0:
														return 'True'
													elif obj[7]<=0:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															return 'False'
														elif obj[2]>0:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[17]>3.0:
											# {"feature": "Carryaway", "instances": 14, "metric_value": 0.9403, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[8]<=5:
													# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.684, "depth": 13}
													if obj[9]>0:
														return 'True'
													elif obj[9]<=0:
														# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[2]<=1:
															# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[4]<=1:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[11]<=1:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=3.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=4.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[7]>0:
																return 'True'
															else: return 'True'
														elif obj[2]>1:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[8]>5:
													return 'False'
												else: return 'False'
											elif obj[16]<=2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[13]<=2:
										# {"feature": "Restaurant20to50", "instances": 60, "metric_value": 0.754, "depth": 10}
										if obj[18]<=2.0:
											# {"feature": "Bar", "instances": 51, "metric_value": 0.819, "depth": 11}
											if obj[14]>0.0:
												# {"feature": "Education", "instances": 32, "metric_value": 0.9284, "depth": 12}
												if obj[11]>0:
													# {"feature": "Carryaway", "instances": 23, "metric_value": 0.7554, "depth": 13}
													if obj[16]<=3.0:
														# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.4855, "depth": 14}
														if obj[17]>2.0:
															# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 15}
															if obj[8]<=3:
																# {"feature": "Weather", "instances": 9, "metric_value": 0.5033, "depth": 16}
																if obj[2]<=1:
																	return 'False'
																elif obj[2]>1:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		return 'False'
																	elif obj[7]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[8]>3:
																return 'True'
															else: return 'True'
														elif obj[17]<=2.0:
															return 'False'
														else: return 'False'
													elif obj[16]>3.0:
														# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8]<=3:
															return 'True'
														elif obj[8]>3:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[11]<=0:
													# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Carryaway", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[16]<=2.0:
															return 'False'
														elif obj[16]>2.0:
															return 'True'
														else: return 'True'
													elif obj[7]>0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[14]<=0.0:
												# {"feature": "Education", "instances": 19, "metric_value": 0.4855, "depth": 12}
												if obj[11]<=2:
													return 'False'
												elif obj[11]>2:
													# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[8]>2:
														# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[9]>0:
																# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[4]<=1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=2.0:
																					# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[17]<=3.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[9]<=0:
																return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'False'
														else: return 'False'
													elif obj[8]<=2:
														return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[18]>2.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[20]<=1:
									# {"feature": "Maritalstatus", "instances": 40, "metric_value": 0.9928, "depth": 9}
									if obj[9]>0:
										# {"feature": "Children", "instances": 25, "metric_value": 0.9044, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Bar", "instances": 21, "metric_value": 0.9587, "depth": 11}
											if obj[14]>0.0:
												# {"feature": "Carryaway", "instances": 16, "metric_value": 0.8113, "depth": 12}
												if obj[16]>2.0:
													# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 13}
													if obj[8]>0:
														# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[7]<=0:
															# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=2:
																return 'False'
															elif obj[13]>2:
																# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[18]<=1.0:
																	return 'False'
																elif obj[18]>1.0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[7]>0:
															# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[13]>2:
																# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[18]<=1.0:
																	return 'False'
																elif obj[18]>1.0:
																	return 'True'
																else: return 'True'
															elif obj[13]<=2:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[8]<=0:
														return 'False'
													else: return 'False'
												elif obj[16]<=2.0:
													return 'False'
												else: return 'False'
											elif obj[14]<=0.0:
												# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[11]>0:
													return 'True'
												elif obj[11]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[10]>0:
											return 'False'
										else: return 'False'
									elif obj[9]<=0:
										# {"feature": "Age", "instances": 15, "metric_value": 0.9183, "depth": 10}
										if obj[8]>1:
											# {"feature": "Carryaway", "instances": 11, "metric_value": 0.684, "depth": 11}
											if obj[16]<=3.0:
												# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[17]>2.0:
													return 'True'
												elif obj[17]<=2.0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7]>0:
														return 'True'
													elif obj[7]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]>3.0:
												return 'False'
											else: return 'False'
										elif obj[8]<=1:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											elif obj[7]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[12]<=0:
								# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]<=6:
									return 'True'
								elif obj[8]>6:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[15]<=1.0:
							# {"feature": "Education", "instances": 216, "metric_value": 0.6281, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Restaurantlessthan20", "instances": 188, "metric_value": 0.6819, "depth": 8}
								if obj[17]>1.0:
									# {"feature": "Restaurant20to50", "instances": 137, "metric_value": 0.5612, "depth": 9}
									if obj[18]>0.0:
										# {"feature": "Bar", "instances": 111, "metric_value": 0.6395, "depth": 10}
										if obj[14]>0.0:
											# {"feature": "Age", "instances": 64, "metric_value": 0.3373, "depth": 11}
											if obj[8]<=3:
												return 'False'
											elif obj[8]>3:
												# {"feature": "Occupation", "instances": 26, "metric_value": 0.6194, "depth": 12}
												if obj[12]>1:
													# {"feature": "Income", "instances": 23, "metric_value": 0.4262, "depth": 13}
													if obj[13]<=3:
														# {"feature": "Carryaway", "instances": 13, "metric_value": 0.6194, "depth": 14}
														if obj[16]>2.0:
															# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Temperature", "instances": 7, "metric_value": 0.5917, "depth": 16}
																if obj[3]<=55:
																	return 'False'
																elif obj[3]>55:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[4]<=0:
																			# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[7]>0:
																return 'True'
															else: return 'True'
														elif obj[16]<=2.0:
															return 'False'
														else: return 'False'
													elif obj[13]>3:
														return 'False'
													else: return 'False'
												elif obj[12]<=1:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7]<=0:
														return 'True'
													elif obj[7]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[14]<=0.0:
											# {"feature": "Time", "instances": 47, "metric_value": 0.8787, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Income", "instances": 34, "metric_value": 0.9597, "depth": 12}
												if obj[13]>1:
													# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 13}
													if obj[12]<=13:
														# {"feature": "Weather", "instances": 27, "metric_value": 0.9751, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Carryaway", "instances": 22, "metric_value": 0.9024, "depth": 15}
															if obj[16]>-1.0:
																# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.8631, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Distance", "instances": 18, "metric_value": 0.9183, "depth": 17}
																	if obj[20]<=2:
																		# {"feature": "Age", "instances": 12, "metric_value": 0.8113, "depth": 18}
																		if obj[8]<=3:
																			# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[3]<=55:
																					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[10]<=1:
																						return 'False'
																					else: return 'False'
																				elif obj[3]>55:
																					return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=55:
																						return 'False'
																					elif obj[3]>55:
																						return 'False'
																					else: return 'False'
																				elif obj[10]<=0:
																					return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[8]>3:
																			return 'False'
																		else: return 'False'
																	elif obj[20]>2:
																		# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 18}
																		if obj[8]>1:
																			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[7]>0:
																				return 'False'
																			elif obj[7]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					return 'True'
																				elif obj[10]>0:
																					return 'False'
																				else: return 'False'
																			else: return 'True'
																		elif obj[8]<=1:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[9]>1:
																	return 'False'
																else: return 'False'
															elif obj[16]<=-1.0:
																return 'True'
															else: return 'True'
														elif obj[2]>0:
															# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[10]<=0:
																return 'True'
															elif obj[10]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[12]>13:
														return 'True'
													else: return 'True'
												elif obj[13]<=1:
													return 'False'
												else: return 'False'
											elif obj[4]>1:
												# {"feature": "Age", "instances": 13, "metric_value": 0.3912, "depth": 12}
												if obj[8]<=5:
													return 'False'
												elif obj[8]>5:
													# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2]>0:
														return 'True'
													elif obj[2]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[18]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[17]<=1.0:
									# {"feature": "Age", "instances": 51, "metric_value": 0.8974, "depth": 9}
									if obj[8]<=4:
										# {"feature": "Income", "instances": 41, "metric_value": 0.965, "depth": 10}
										if obj[13]>0:
											# {"feature": "Restaurant20to50", "instances": 38, "metric_value": 0.9268, "depth": 11}
											if obj[18]<=1.0:
												# {"feature": "Occupation", "instances": 31, "metric_value": 0.8238, "depth": 12}
												if obj[12]>5:
													# {"feature": "Carryaway", "instances": 17, "metric_value": 0.5226, "depth": 13}
													if obj[16]>1.0:
														return 'False'
													elif obj[16]<=1.0:
														# {"feature": "Temperature", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[20]<=2:
																return 'False'
															elif obj[20]>2:
																# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[2]>0:
																	return 'True'
																elif obj[2]<=0:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[3]>55:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[12]<=5:
													# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 13}
													if obj[14]<=0.0:
														# {"feature": "Weather", "instances": 11, "metric_value": 0.994, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Carryaway", "instances": 9, "metric_value": 0.9911, "depth": 15}
															if obj[16]<=2.0:
																# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[20]<=2:
																			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[4]<=1:
																				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[7]<=1:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[20]>2:
																			return 'True'
																		else: return 'True'
																	elif obj[9]>0:
																		return 'False'
																	else: return 'False'
																elif obj[3]>55:
																	return 'False'
																else: return 'False'
															elif obj[16]>2.0:
																return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'True'
														else: return 'True'
													elif obj[14]>0.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[18]>1.0:
												# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[2]<=0:
													return 'True'
												elif obj[2]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[13]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]>4:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[11]>2:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]<=0:
						# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[8]>0:
							return 'True'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[19]>0:
					# {"feature": "Time", "instances": 439, "metric_value": 0.9886, "depth": 5}
					if obj[4]>0:
						# {"feature": "Coffeehouse", "instances": 304, "metric_value": 0.9992, "depth": 6}
						if obj[15]<=1.0:
							# {"feature": "Distance", "instances": 152, "metric_value": 0.9591, "depth": 7}
							if obj[20]<=1:
								# {"feature": "Maritalstatus", "instances": 101, "metric_value": 0.9914, "depth": 8}
								if obj[9]<=2:
									# {"feature": "Weather", "instances": 96, "metric_value": 0.9799, "depth": 9}
									if obj[2]<=0:
										# {"feature": "Carryaway", "instances": 79, "metric_value": 0.999, "depth": 10}
										if obj[16]>1.0:
											# {"feature": "Restaurantlessthan20", "instances": 57, "metric_value": 0.9944, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Age", "instances": 45, "metric_value": 0.9968, "depth": 12}
												if obj[8]<=5:
													# {"feature": "Income", "instances": 39, "metric_value": 0.9995, "depth": 13}
													if obj[13]<=5:
														# {"feature": "Occupation", "instances": 26, "metric_value": 0.9829, "depth": 14}
														if obj[12]>1:
															# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.9457, "depth": 15}
															if obj[18]>-1.0:
																# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 16}
																if obj[11]>0:
																	# {"feature": "Bar", "instances": 15, "metric_value": 0.971, "depth": 17}
																	if obj[14]<=1.0:
																		# {"feature": "Children", "instances": 12, "metric_value": 0.9183, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[3]<=80:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[3]<=80:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=80:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[14]>1.0:
																		# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[11]<=0:
																	# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[10]<=0:
																		return 'False'
																	elif obj[10]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[18]<=-1.0:
																return 'True'
															else: return 'True'
														elif obj[12]<=1:
															# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[7]<=0:
																return 'True'
															elif obj[7]>0:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[11]<=0:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=0.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[13]>5:
														# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 14}
														if obj[12]<=10:
															# {"feature": "Children", "instances": 12, "metric_value": 0.8113, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 16}
																if obj[14]>0.0:
																	# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[7]>0:
																		return 'True'
																	elif obj[7]<=0:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=2:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[14]<=0.0:
																	# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		return 'True'
																	elif obj[7]>0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[10]>0:
																return 'True'
															else: return 'True'
														elif obj[12]>10:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[8]>5:
													# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11]>2:
															return 'False'
														elif obj[11]<=2:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'False'
											elif obj[17]<=1.0:
												# {"feature": "Income", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[13]>2:
													return 'True'
												elif obj[13]<=2:
													# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[14]<=0.0:
														return 'True'
													elif obj[14]>0.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[16]<=1.0:
											# {"feature": "Age", "instances": 22, "metric_value": 0.9024, "depth": 11}
											if obj[8]>1:
												# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 12}
												if obj[12]<=13:
													# {"feature": "Education", "instances": 15, "metric_value": 0.5665, "depth": 13}
													if obj[11]>1:
														return 'False'
													elif obj[11]<=1:
														# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[17]<=2.0:
															# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[13]<=3:
																# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[3]<=80:
																		# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[14]<=0.0:
																					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[18]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[13]>3:
																return 'True'
															else: return 'True'
														elif obj[17]>2.0:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[12]>13:
													return 'True'
												else: return 'True'
											elif obj[8]<=1:
												# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=2:
													return 'True'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'False'
									elif obj[2]>0:
										# {"feature": "Income", "instances": 17, "metric_value": 0.5226, "depth": 10}
										if obj[13]<=7:
											# {"feature": "Restaurantlessthan20", "instances": 16, "metric_value": 0.3373, "depth": 11}
											if obj[17]>0.0:
												return 'False'
											elif obj[17]<=0.0:
												# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]>0:
													return 'False'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[13]>7:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>2:
									return 'True'
								else: return 'True'
							elif obj[20]>1:
								# {"feature": "Bar", "instances": 51, "metric_value": 0.819, "depth": 8}
								if obj[14]<=1.0:
									# {"feature": "Education", "instances": 42, "metric_value": 0.8926, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Occupation", "instances": 30, "metric_value": 0.971, "depth": 10}
										if obj[12]<=14:
											# {"feature": "Children", "instances": 27, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Temperature", "instances": 14, "metric_value": 0.5917, "depth": 12}
												if obj[3]<=55:
													return 'False'
												elif obj[3]>55:
													# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[18]>0.0:
														# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[9]<=1:
															return 'False'
														elif obj[9]>1:
															# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[8]>1:
																return 'True'
															elif obj[8]<=1:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[18]<=0.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[10]>0:
												# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 12}
												if obj[13]<=3:
													# {"feature": "Carryaway", "instances": 10, "metric_value": 0.971, "depth": 13}
													if obj[16]>1.0:
														# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 14}
														if obj[1]>0:
															# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[17]<=3.0:
																# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[8]<=4:
																	return 'True'
																elif obj[8]>4:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]<=0:
																		return 'False'
																	elif obj[7]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[17]>3.0:
																return 'False'
															else: return 'False'
														elif obj[1]<=0:
															return 'False'
														else: return 'False'
													elif obj[16]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[13]>3:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]>14:
											return 'True'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Income", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[13]>0:
											return 'False'
										elif obj[13]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[14]>1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[15]>1.0:
							# {"feature": "Age", "instances": 152, "metric_value": 0.9788, "depth": 7}
							if obj[8]<=5:
								# {"feature": "Restaurantlessthan20", "instances": 128, "metric_value": 0.9937, "depth": 8}
								if obj[17]>2.0:
									# {"feature": "Weather", "instances": 73, "metric_value": 0.9395, "depth": 9}
									if obj[2]<=0:
										# {"feature": "Distance", "instances": 54, "metric_value": 0.8767, "depth": 10}
										if obj[20]<=1:
											# {"feature": "Occupation", "instances": 41, "metric_value": 0.9474, "depth": 11}
											if obj[12]<=13:
												# {"feature": "Carryaway", "instances": 37, "metric_value": 0.974, "depth": 12}
												if obj[16]>2.0:
													# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.8865, "depth": 13}
													if obj[18]<=3.0:
														# {"feature": "Education", "instances": 21, "metric_value": 0.9183, "depth": 14}
														if obj[11]>0:
															# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.971, "depth": 15}
															if obj[9]>0:
																# {"feature": "Income", "instances": 11, "metric_value": 0.994, "depth": 16}
																if obj[13]>0:
																	# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 17}
																	if obj[14]>0.0:
																		# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[14]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[13]<=0:
																	return 'False'
																else: return 'False'
															elif obj[9]<=0:
																# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[13]>1:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=0.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[13]<=1:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[11]<=0:
															# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[10]<=0:
																return 'True'
															elif obj[10]>0:
																# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[13]<=3:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[7]<=1:
																				# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[9]<=0:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[13]>3:
																	return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[18]>3.0:
														return 'True'
													else: return 'True'
												elif obj[16]<=2.0:
													# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 13}
													if obj[11]<=2:
														# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 14}
														if obj[18]<=3.0:
															# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 15}
															if obj[13]>0:
																# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[9]>0:
																	# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[14]>0.0:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[14]<=0.0:
																			return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[9]<=0:
																	return 'False'
																else: return 'False'
															elif obj[13]<=0:
																# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[14]>1.0:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[9]<=1:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[14]<=1.0:
																		return 'False'
																	else: return 'False'
																elif obj[7]>0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[18]>3.0:
															return 'False'
														else: return 'False'
													elif obj[11]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[12]>13:
												return 'True'
											else: return 'True'
										elif obj[20]>1:
											# {"feature": "Income", "instances": 13, "metric_value": 0.3912, "depth": 11}
											if obj[13]>0:
												return 'True'
											elif obj[13]<=0:
												# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[12]>5:
													return 'False'
												elif obj[12]<=5:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									elif obj[2]>0:
										# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 10}
										if obj[12]<=6:
											# {"feature": "Income", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[13]<=5:
												return 'False'
											elif obj[13]>5:
												# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[14]<=0.0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]<=55:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=0:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=3.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=0.0:
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
													elif obj[7]>0:
														return 'False'
													else: return 'False'
												elif obj[14]>0.0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[12]>6:
											# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[11]<=2:
												return 'True'
											elif obj[11]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[17]<=2.0:
									# {"feature": "Education", "instances": 55, "metric_value": 0.9806, "depth": 9}
									if obj[11]<=3:
										# {"feature": "Carryaway", "instances": 50, "metric_value": 0.9954, "depth": 10}
										if obj[16]>1.0:
											# {"feature": "Occupation", "instances": 46, "metric_value": 1.0, "depth": 11}
											if obj[12]<=12:
												# {"feature": "Maritalstatus", "instances": 43, "metric_value": 0.9965, "depth": 12}
												if obj[9]>0:
													# {"feature": "Gender", "instances": 35, "metric_value": 0.9947, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9819, "depth": 14}
														if obj[18]>0.0:
															# {"feature": "Income", "instances": 16, "metric_value": 1.0, "depth": 15}
															if obj[13]<=6:
																# {"feature": "Bar", "instances": 15, "metric_value": 0.9968, "depth": 16}
																if obj[14]>0.0:
																	# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 17}
																	if obj[20]<=1:
																		# {"feature": "Children", "instances": 8, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 19}
																			if obj[2]>0:
																				# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[3]<=55:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[2]<=0:
																				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=80:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[20]>1:
																		# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[3]<=80:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[14]<=0.0:
																	# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[20]<=1:
																		# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[20]>1:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[13]>6:
																return 'False'
															else: return 'False'
														elif obj[18]<=0.0:
															return 'True'
														else: return 'True'
													elif obj[7]>0:
														# {"feature": "Weather", "instances": 16, "metric_value": 0.896, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Income", "instances": 15, "metric_value": 0.8366, "depth": 15}
															if obj[13]<=7:
																# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 16}
																if obj[18]>0.0:
																	# {"feature": "Bar", "instances": 7, "metric_value": 0.8631, "depth": 17}
																	if obj[14]>0.0:
																		# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[3]<=80:
																					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[14]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[18]<=0.0:
																	return 'False'
																else: return 'False'
															elif obj[13]>7:
																# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[14]>0.0:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[3]<=80:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=0.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[14]<=0.0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[9]<=0:
													# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[2]<=0:
														return 'True'
													elif obj[2]>0:
														# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[20]>1:
															return 'False'
														elif obj[20]<=1:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											elif obj[12]>12:
												return 'False'
											else: return 'False'
										elif obj[16]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[11]>3:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]>5:
								# {"feature": "Income", "instances": 24, "metric_value": 0.7383, "depth": 8}
								if obj[13]<=3:
									# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[20]<=1:
										# {"feature": "Carryaway", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[16]>2.0:
											# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[12]>4:
												# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[7]<=0:
													# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[1]<=1:
														# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[3]<=80:
																# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[9]>1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=1:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=2.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[9]<=1:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=1.0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[7]>0:
													return 'False'
												else: return 'False'
											elif obj[12]<=4:
												return 'False'
											else: return 'False'
										elif obj[16]<=2.0:
											return 'True'
										else: return 'True'
									elif obj[20]>1:
										return 'True'
									else: return 'True'
								elif obj[13]>3:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]<=0:
						# {"feature": "Restaurant20to50", "instances": 135, "metric_value": 0.8256, "depth": 6}
						if obj[18]<=1.0:
							# {"feature": "Distance", "instances": 94, "metric_value": 0.8914, "depth": 7}
							if obj[20]>1:
								# {"feature": "Carryaway", "instances": 57, "metric_value": 0.7746, "depth": 8}
								if obj[16]<=3.0:
									# {"feature": "Education", "instances": 48, "metric_value": 0.65, "depth": 9}
									if obj[11]>0:
										# {"feature": "Coffeehouse", "instances": 35, "metric_value": 0.7755, "depth": 10}
										if obj[15]>0.0:
											# {"feature": "Income", "instances": 24, "metric_value": 0.5436, "depth": 11}
											if obj[13]<=4:
												return 'True'
											elif obj[13]>4:
												# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[8]>1:
													# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[12]>4:
														# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[9]<=1:
															return 'False'
														elif obj[9]>1:
															return 'True'
														else: return 'True'
													elif obj[12]<=4:
														return 'True'
													else: return 'True'
												elif obj[8]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[15]<=0.0:
											# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 11}
											if obj[12]>1:
												# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[8]>0:
													return 'True'
												elif obj[8]<=0:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]>30:
														return 'False'
													elif obj[3]<=30:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[12]<=1:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]<=0:
										return 'True'
									else: return 'True'
								elif obj[16]>3.0:
									# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[11]<=1:
										# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[12]<=19:
											return 'False'
										elif obj[12]>19:
											return 'True'
										else: return 'True'
									elif obj[11]>1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[20]<=1:
								# {"feature": "Maritalstatus", "instances": 37, "metric_value": 0.9868, "depth": 8}
								if obj[9]>0:
									# {"feature": "Coffeehouse", "instances": 28, "metric_value": 0.9059, "depth": 9}
									if obj[15]<=3.0:
										# {"feature": "Income", "instances": 26, "metric_value": 0.8404, "depth": 10}
										if obj[13]<=3:
											# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 11}
											if obj[12]<=16:
												# {"feature": "Bar", "instances": 15, "metric_value": 0.9968, "depth": 12}
												if obj[14]<=2.0:
													# {"feature": "Children", "instances": 13, "metric_value": 0.9957, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[7]>0:
															# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[8]>1:
																# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[11]>0:
																	# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[17]>2.0:
																		return 'False'
																	elif obj[17]<=2.0:
																		return 'True'
																	else: return 'True'
																elif obj[11]<=0:
																	return 'False'
																else: return 'False'
															elif obj[8]<=1:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[8]>1:
																# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[16]<=2.0:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[2]<=0:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=80:
																				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=0:
																					# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[17]<=2.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[16]>2.0:
																	return 'False'
																else: return 'False'
															elif obj[8]<=1:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[10]>0:
														# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8]<=2:
															# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11]>2:
																return 'False'
															elif obj[11]<=2:
																return 'True'
															else: return 'True'
														elif obj[8]>2:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[14]>2.0:
													return 'True'
												else: return 'True'
											elif obj[12]>16:
												return 'True'
											else: return 'True'
										elif obj[13]>3:
											return 'True'
										else: return 'True'
									elif obj[15]>3.0:
										return 'False'
									else: return 'False'
								elif obj[9]<=0:
									# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[15]<=1.0:
										return 'False'
									elif obj[15]>1.0:
										# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[17]<=2.0:
											return 'True'
										elif obj[17]>2.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[18]>1.0:
							# {"feature": "Bar", "instances": 41, "metric_value": 0.6006, "depth": 7}
							if obj[14]<=3.0:
								# {"feature": "Gender", "instances": 40, "metric_value": 0.5436, "depth": 8}
								if obj[7]>0:
									return 'True'
								elif obj[7]<=0:
									# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 9}
									if obj[12]<=7:
										# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[15]>0.0:
											# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.8813, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[8]<=3:
													return 'True'
												elif obj[8]>3:
													# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[20]>1:
														return 'False'
													elif obj[20]<=1:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[17]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[15]<=0.0:
											return 'False'
										else: return 'False'
									elif obj[12]>7:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[14]>3.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[6]<=0:
			# {"feature": "Coffeehouse", "instances": 1782, "metric_value": 0.8547, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Driving_to", "instances": 1322, "metric_value": 0.7845, "depth": 4}
				if obj[0]<=0:
					# {"feature": "Time", "instances": 700, "metric_value": 0.6985, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Temperature", "instances": 403, "metric_value": 0.607, "depth": 6}
						if obj[3]>55:
							# {"feature": "Bar", "instances": 216, "metric_value": 0.7107, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Maritalstatus", "instances": 130, "metric_value": 0.8051, "depth": 8}
								if obj[9]>0:
									# {"feature": "Age", "instances": 68, "metric_value": 0.6385, "depth": 9}
									if obj[8]<=5:
										# {"feature": "Education", "instances": 55, "metric_value": 0.4972, "depth": 10}
										if obj[11]<=1:
											# {"feature": "Occupation", "instances": 29, "metric_value": 0.7355, "depth": 11}
											if obj[12]<=19:
												# {"feature": "Income", "instances": 28, "metric_value": 0.6769, "depth": 12}
												if obj[13]<=6:
													# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.7732, "depth": 13}
													if obj[18]<=1.0:
														# {"feature": "Gender", "instances": 18, "metric_value": 0.8524, "depth": 14}
														if obj[7]>0:
															# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.971, "depth": 15}
															if obj[17]<=2.0:
																# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 16}
																if obj[1]>2:
																	# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[20]>1:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[10]>0:
																			return 'True'
																		elif obj[10]<=0:
																			# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]>1.0:
																				return 'False'
																			elif obj[16]<=1.0:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	elif obj[20]<=1:
																		return 'False'
																	else: return 'False'
																elif obj[1]<=2:
																	return 'True'
																else: return 'True'
															elif obj[17]>2.0:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															# {"feature": "Children", "instances": 8, "metric_value": 0.5436, "depth": 15}
															if obj[10]<=0:
																return 'True'
															elif obj[10]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[18]>1.0:
														return 'True'
													else: return 'True'
												elif obj[13]>6:
													return 'True'
												else: return 'True'
											elif obj[12]>19:
												return 'False'
											else: return 'False'
										elif obj[11]>1:
											return 'True'
										else: return 'True'
									elif obj[8]>5:
										# {"feature": "Income", "instances": 13, "metric_value": 0.9612, "depth": 10}
										if obj[13]>0:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[18]<=1.0:
												# {"feature": "Carryaway", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[16]>2.0:
													return 'True'
												elif obj[16]<=2.0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[20]>1:
														# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1]<=3:
															# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[11]<=0:
																			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[12]<=7:
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
													elif obj[20]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[18]>1.0:
												# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[20]<=1:
													return 'False'
												elif obj[20]>1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[13]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[9]<=0:
									# {"feature": "Carryaway", "instances": 62, "metric_value": 0.9236, "depth": 9}
									if obj[16]<=2.0:
										# {"feature": "Passanger", "instances": 32, "metric_value": 0.7579, "depth": 10}
										if obj[1]>2:
											# {"feature": "Occupation", "instances": 21, "metric_value": 0.9183, "depth": 11}
											if obj[12]<=6:
												# {"feature": "Income", "instances": 12, "metric_value": 1.0, "depth": 12}
												if obj[13]>2:
													# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[8]<=6:
														return 'True'
													elif obj[8]>6:
														# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[7]>0:
															return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[13]<=2:
													return 'False'
												else: return 'False'
											elif obj[12]>6:
												# {"feature": "Gender", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[7]>0:
													return 'True'
												elif obj[7]<=0:
													# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[8]>4:
														# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[17]>1.0:
															return 'False'
														elif obj[17]<=1.0:
															return 'True'
														else: return 'True'
													elif obj[8]<=4:
														return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[1]<=2:
											return 'True'
										else: return 'True'
									elif obj[16]>2.0:
										# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9968, "depth": 10}
										if obj[18]<=1.0:
											# {"feature": "Income", "instances": 19, "metric_value": 0.9819, "depth": 11}
											if obj[13]>3:
												# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 12}
												if obj[8]>0:
													# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 13}
													if obj[1]>0:
														# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 14}
														if obj[20]<=1:
															# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[12]<=4:
																return 'True'
															elif obj[12]>4:
																# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[17]<=2.0:
																	return 'False'
																elif obj[17]>2.0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[20]>1:
															# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[10]>0:
																return 'False'
															elif obj[10]<=0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[1]<=0:
														return 'False'
													else: return 'False'
												elif obj[8]<=0:
													return 'True'
												else: return 'True'
											elif obj[13]<=3:
												# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[12]>1:
													return 'False'
												elif obj[12]<=1:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[18]>1.0:
											# {"feature": "Children", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[10]>0:
												# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[12]<=12:
													# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[8]<=2:
														# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1]<=2:
															return 'False'
														elif obj[1]>2:
															return 'True'
														else: return 'True'
													elif obj[8]>2:
														# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1]<=2:
															return 'True'
														elif obj[1]>2:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[12]>12:
													return 'True'
												else: return 'True'
											elif obj[10]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[14]>1.0:
								# {"feature": "Passanger", "instances": 86, "metric_value": 0.5186, "depth": 8}
								if obj[1]>2:
									# {"feature": "Maritalstatus", "instances": 76, "metric_value": 0.5618, "depth": 9}
									if obj[9]<=2:
										# {"feature": "Restaurantlessthan20", "instances": 75, "metric_value": 0.5294, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Occupation", "instances": 70, "metric_value": 0.469, "depth": 11}
											if obj[12]>4:
												# {"feature": "Restaurant20to50", "instances": 54, "metric_value": 0.5564, "depth": 12}
												if obj[18]<=3.0:
													# {"feature": "Carryaway", "instances": 49, "metric_value": 0.5917, "depth": 13}
													if obj[16]<=3.0:
														# {"feature": "Age", "instances": 43, "metric_value": 0.5186, "depth": 14}
														if obj[8]>1:
															# {"feature": "Distance", "instances": 23, "metric_value": 0.258, "depth": 15}
															if obj[20]>1:
																return 'True'
															elif obj[20]<=1:
																# {"feature": "Income", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[13]<=2:
																	return 'True'
																elif obj[13]>2:
																	# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[10]>0:
																		return 'True'
																	elif obj[10]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															else: return 'True'
														elif obj[8]<=1:
															# {"feature": "Income", "instances": 20, "metric_value": 0.7219, "depth": 15}
															if obj[13]<=6:
																# {"feature": "Distance", "instances": 19, "metric_value": 0.6292, "depth": 16}
																if obj[20]>1:
																	# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 17}
																	if obj[11]<=2:
																		# {"feature": "Gender", "instances": 11, "metric_value": 0.684, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				return 'False'
																			else: return 'False'
																		else: return 'True'
																	elif obj[11]>2:
																		return 'False'
																	else: return 'False'
																elif obj[20]<=1:
																	return 'True'
																else: return 'True'
															elif obj[13]>6:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[16]>3.0:
														# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 14}
														if obj[8]<=1:
															return 'True'
														elif obj[8]>1:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[18]>3.0:
													return 'True'
												else: return 'True'
											elif obj[12]<=4:
												return 'True'
											else: return 'True'
										elif obj[17]<=1.0:
											# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[11]>0:
												return 'True'
											elif obj[11]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[9]>2:
										return 'False'
									else: return 'False'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=55:
							# {"feature": "Restaurant20to50", "instances": 187, "metric_value": 0.457, "depth": 7}
							if obj[18]<=3.0:
								# {"feature": "Weather", "instances": 184, "metric_value": 0.4262, "depth": 8}
								if obj[2]<=0:
									# {"feature": "Maritalstatus", "instances": 162, "metric_value": 0.4651, "depth": 9}
									if obj[9]>0:
										# {"feature": "Gender", "instances": 81, "metric_value": 0.5731, "depth": 10}
										if obj[7]>0:
											# {"feature": "Income", "instances": 44, "metric_value": 0.3591, "depth": 11}
											if obj[13]>3:
												return 'True'
											elif obj[13]<=3:
												# {"feature": "Passanger", "instances": 20, "metric_value": 0.6098, "depth": 12}
												if obj[1]>2:
													# {"feature": "Children", "instances": 13, "metric_value": 0.7793, "depth": 13}
													if obj[10]<=0:
														# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[17]>1.0:
															return 'True'
														elif obj[17]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[10]>0:
														# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[12]<=7:
															return 'False'
														elif obj[12]>7:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[1]<=2:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[7]<=0:
											# {"feature": "Carryaway", "instances": 37, "metric_value": 0.7532, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.5586, "depth": 12}
												if obj[17]<=2.0:
													# {"feature": "Passanger", "instances": 14, "metric_value": 0.7496, "depth": 13}
													if obj[1]>2:
														# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[12]<=11:
															# {"feature": "Bar", "instances": 9, "metric_value": 0.7642, "depth": 15}
															if obj[14]<=1.0:
																return 'True'
															elif obj[14]>1.0:
																# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[8]>0:
																	return 'False'
																elif obj[8]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[12]>11:
															return 'False'
														else: return 'False'
													elif obj[1]<=2:
														return 'True'
													else: return 'True'
												elif obj[17]>2.0:
													return 'True'
												else: return 'True'
											elif obj[16]<=2.0:
												# {"feature": "Age", "instances": 14, "metric_value": 0.9403, "depth": 12}
												if obj[8]>1:
													# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.8113, "depth": 13}
													if obj[17]>1.0:
														return 'True'
													elif obj[17]<=1.0:
														# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[11]>0:
															# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[1]>1:
																return 'True'
															elif obj[1]<=1:
																return 'False'
															else: return 'False'
														elif obj[11]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[8]<=1:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									elif obj[9]<=0:
										# {"feature": "Passanger", "instances": 81, "metric_value": 0.3343, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Distance", "instances": 53, "metric_value": 0.4508, "depth": 11}
											if obj[20]>1:
												# {"feature": "Education", "instances": 31, "metric_value": 0.6374, "depth": 12}
												if obj[11]>0:
													# {"feature": "Occupation", "instances": 20, "metric_value": 0.8113, "depth": 13}
													if obj[12]<=12:
														# {"feature": "Income", "instances": 19, "metric_value": 0.7425, "depth": 14}
														if obj[13]>3:
															# {"feature": "Age", "instances": 13, "metric_value": 0.8905, "depth": 15}
															if obj[8]>0:
																# {"feature": "Gender", "instances": 12, "metric_value": 0.8113, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Carryaway", "instances": 8, "metric_value": 0.9544, "depth": 17}
																	if obj[16]<=3.0:
																		# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 18}
																		if obj[14]>-1.0:
																			# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[17]>2.0:
																				return 'True'
																			else: return 'True'
																		elif obj[14]<=-1.0:
																			return 'True'
																		else: return 'True'
																	elif obj[16]>3.0:
																		return 'True'
																	else: return 'True'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															elif obj[8]<=0:
																return 'False'
															else: return 'False'
														elif obj[13]<=3:
															return 'True'
														else: return 'True'
													elif obj[12]>12:
														return 'False'
													else: return 'False'
												elif obj[11]<=0:
													return 'True'
												else: return 'True'
											elif obj[20]<=1:
												return 'True'
											else: return 'True'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							elif obj[18]>3.0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>1:
									return 'False'
								elif obj[1]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[4]>2:
						# {"feature": "Education", "instances": 297, "metric_value": 0.799, "depth": 6}
						if obj[11]>0:
							# {"feature": "Maritalstatus", "instances": 202, "metric_value": 0.8584, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Occupation", "instances": 153, "metric_value": 0.7871, "depth": 8}
								if obj[12]<=19.76471814820038:
									# {"feature": "Age", "instances": 143, "metric_value": 0.7411, "depth": 9}
									if obj[8]>0:
										# {"feature": "Children", "instances": 125, "metric_value": 0.6887, "depth": 10}
										if obj[10]<=0:
											# {"feature": "Bar", "instances": 71, "metric_value": 0.8168, "depth": 11}
											if obj[14]<=3.0:
												# {"feature": "Restaurant20to50", "instances": 70, "metric_value": 0.7998, "depth": 12}
												if obj[18]>-1.0:
													# {"feature": "Carryaway", "instances": 69, "metric_value": 0.7813, "depth": 13}
													if obj[16]>-1.0:
														# {"feature": "Income", "instances": 66, "metric_value": 0.7455, "depth": 14}
														if obj[13]<=7:
															# {"feature": "Passanger", "instances": 63, "metric_value": 0.7642, "depth": 15}
															if obj[1]>1:
																# {"feature": "Temperature", "instances": 32, "metric_value": 0.8571, "depth": 16}
																if obj[3]<=30:
																	# {"feature": "Weather", "instances": 21, "metric_value": 0.9587, "depth": 17}
																	if obj[2]>0:
																		# {"feature": "Gender", "instances": 19, "metric_value": 0.8997, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.9799, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Direction_same", "instances": 10, "metric_value": 0.8813, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[17]>2.0:
																				return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.5917, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[17]>2.0:
																				return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[2]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[3]>30:
																	# {"feature": "Restaurantlessthan20", "instances": 11, "metric_value": 0.4395, "depth": 17}
																	if obj[17]>1.0:
																		# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[20]>1:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[20]<=1:
																				return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[17]<=1.0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[1]<=1:
																# {"feature": "Gender", "instances": 31, "metric_value": 0.6374, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Weather", "instances": 18, "metric_value": 0.3095, "depth": 17}
																	if obj[2]<=0:
																		return 'True'
																	elif obj[2]>0:
																		# {"feature": "Temperature", "instances": 7, "metric_value": 0.5917, "depth": 18}
																		if obj[3]<=30:
																			return 'True'
																		elif obj[3]>30:
																			# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=3.0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	# {"feature": "Temperature", "instances": 13, "metric_value": 0.8905, "depth": 17}
																	if obj[3]>30:
																		# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 18}
																		if obj[20]>1:
																			# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.8631, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[2]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[17]>2.0:
																				return 'True'
																			else: return 'True'
																		elif obj[20]<=1:
																			# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[17]<=2.0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[17]>2.0:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[3]<=30:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[13]>7:
															return 'True'
														else: return 'True'
													elif obj[16]<=-1.0:
														# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1]>0:
															# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[2]<=0:
																return 'True'
															elif obj[2]>0:
																return 'False'
															else: return 'False'
														elif obj[1]<=0:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[18]<=-1.0:
													return 'False'
												else: return 'False'
											elif obj[14]>3.0:
												return 'False'
											else: return 'False'
										elif obj[10]>0:
											# {"feature": "Bar", "instances": 54, "metric_value": 0.4451, "depth": 11}
											if obj[14]<=1.0:
												# {"feature": "Weather", "instances": 38, "metric_value": 0.5618, "depth": 12}
												if obj[2]<=1:
													# {"feature": "Temperature", "instances": 32, "metric_value": 0.6253, "depth": 13}
													if obj[3]>55:
														# {"feature": "Distance", "instances": 22, "metric_value": 0.4395, "depth": 14}
														if obj[20]>1:
															return 'True'
														elif obj[20]<=1:
															# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[18]>1.0:
																return 'True'
															elif obj[18]<=1.0:
																# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[1]>1:
																	return 'False'
																elif obj[1]<=1:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'True'
													elif obj[3]<=55:
														# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[20]>1:
															# {"feature": "Carryaway", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[16]<=2.0:
																# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[17]>2.0:
																	# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			return 'False'
																		elif obj[7]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[1]>1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[17]<=2.0:
																	return 'False'
																else: return 'False'
															elif obj[16]>2.0:
																return 'True'
															else: return 'True'
														elif obj[20]<=1:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[2]>1:
													return 'True'
												else: return 'True'
											elif obj[14]>1.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[8]<=0:
										# {"feature": "Carryaway", "instances": 18, "metric_value": 0.9641, "depth": 10}
										if obj[16]<=3.0:
											# {"feature": "Income", "instances": 15, "metric_value": 0.8366, "depth": 11}
											if obj[13]<=4:
												# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[17]>1.0:
														return 'True'
													elif obj[17]<=1.0:
														# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2]>0:
															return 'True'
														elif obj[2]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[1]>1:
													return 'False'
												else: return 'False'
											elif obj[13]>4:
												return 'True'
											else: return 'True'
										elif obj[16]>3.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]>19.76471814820038:
									# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[13]<=2:
										# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[2]<=1:
											# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=55:
												return 'True'
											elif obj[3]>55:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														return 'True'
													else: return 'True'
												elif obj[1]>1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[2]>1:
											return 'False'
										else: return 'False'
									elif obj[13]>2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[9]>1:
								# {"feature": "Restaurant20to50", "instances": 49, "metric_value": 0.9852, "depth": 8}
								if obj[18]<=1.0:
									# {"feature": "Bar", "instances": 31, "metric_value": 0.8691, "depth": 9}
									if obj[14]>0.0:
										# {"feature": "Passanger", "instances": 18, "metric_value": 1.0, "depth": 10}
										if obj[1]>0:
											# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 11}
											if obj[20]>1:
												# {"feature": "Carryaway", "instances": 12, "metric_value": 0.8113, "depth": 12}
												if obj[16]>1.0:
													# {"feature": "Temperature", "instances": 9, "metric_value": 0.5033, "depth": 13}
													if obj[3]<=55:
														return 'True'
													elif obj[3]>55:
														# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8]<=1:
															return 'True'
														elif obj[8]>1:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[16]<=1.0:
													# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[2]<=0:
														return 'False'
													elif obj[2]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[20]<=1:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[14]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[18]>1.0:
									# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 9}
									if obj[12]<=12:
										# {"feature": "Gender", "instances": 14, "metric_value": 0.7496, "depth": 10}
										if obj[7]>0:
											# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.6194, "depth": 11}
											if obj[17]<=2.0:
												# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[1]>1:
														# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[8]<=0:
															return 'False'
														elif obj[8]>0:
															return 'True'
														else: return 'True'
													elif obj[1]<=1:
														# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]>30:
															return 'True'
														elif obj[3]<=30:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[2]>0:
													return 'False'
												else: return 'False'
											elif obj[17]>2.0:
												return 'False'
											else: return 'False'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									elif obj[12]>12:
										# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[2]<=0:
											return 'True'
										elif obj[2]>0:
											# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[1]<=3:
												# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=30:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]<=0:
														# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8]<=2:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[10]<=1:
																# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13]<=6:
																	# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14]<=0.0:
																		# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]<=3.0:
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
														else: return 'False'
													else: return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=0:
							# {"feature": "Carryaway", "instances": 95, "metric_value": 0.6292, "depth": 7}
							if obj[16]>2.0:
								# {"feature": "Gender", "instances": 52, "metric_value": 0.3182, "depth": 8}
								if obj[7]<=0:
									return 'True'
								elif obj[7]>0:
									# {"feature": "Weather", "instances": 24, "metric_value": 0.5436, "depth": 9}
									if obj[2]<=1:
										# {"feature": "Occupation", "instances": 20, "metric_value": 0.2864, "depth": 10}
										if obj[12]>2:
											return 'True'
										elif obj[12]<=2:
											# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=55:
													return 'True'
												elif obj[3]>55:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[2]>1:
										# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[10]>0:
											return 'False'
										elif obj[10]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[16]<=2.0:
								# {"feature": "Occupation", "instances": 43, "metric_value": 0.8542, "depth": 8}
								if obj[12]>2:
									# {"feature": "Distance", "instances": 33, "metric_value": 0.7455, "depth": 9}
									if obj[20]>1:
										# {"feature": "Maritalstatus", "instances": 25, "metric_value": 0.8555, "depth": 10}
										if obj[9]<=2:
											# {"feature": "Income", "instances": 24, "metric_value": 0.8113, "depth": 11}
											if obj[13]>1:
												# {"feature": "Restaurantlessthan20", "instances": 21, "metric_value": 0.8631, "depth": 12}
												if obj[17]<=3.0:
													# {"feature": "Age", "instances": 19, "metric_value": 0.8997, "depth": 13}
													if obj[8]>1:
														# {"feature": "Bar", "instances": 16, "metric_value": 0.8113, "depth": 14}
														if obj[14]<=2.0:
															# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 15}
															if obj[1]>0:
																# {"feature": "Temperature", "instances": 10, "metric_value": 0.7219, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Weather", "instances": 8, "metric_value": 0.5436, "depth": 17}
																	if obj[2]<=1:
																		return 'True'
																	elif obj[2]>1:
																		# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]>1.0:
																				return 'True'
																			elif obj[18]<=1.0:
																				return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		return 'False'
																	elif obj[10]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[1]<=0:
																return 'True'
															else: return 'True'
														elif obj[14]>2.0:
															# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[1]>0:
																# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[2]<=0:
																	return 'True'
																elif obj[2]>0:
																	return 'False'
																else: return 'False'
															elif obj[1]<=0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[8]<=1:
														# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[1]>2:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]>30:
																return 'True'
															elif obj[3]<=30:
																return 'False'
															else: return 'False'
														elif obj[1]<=2:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[17]>3.0:
													return 'True'
												else: return 'True'
											elif obj[13]<=1:
												return 'True'
											else: return 'True'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[20]<=1:
										return 'True'
									else: return 'True'
								elif obj[12]<=2:
									# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										# {"feature": "Weather", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[2]<=0:
											# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[3]>30:
												# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[8]>2:
													return 'True'
												elif obj[8]<=2:
													return 'False'
												else: return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[2]>0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[0]>0:
					# {"feature": "Distance", "instances": 622, "metric_value": 0.8616, "depth": 5}
					if obj[20]<=1:
						# {"feature": "Income", "instances": 404, "metric_value": 0.7911, "depth": 6}
						if obj[13]<=5:
							# {"feature": "Passanger", "instances": 289, "metric_value": 0.8462, "depth": 7}
							if obj[1]>0:
								# {"feature": "Age", "instances": 271, "metric_value": 0.8242, "depth": 8}
								if obj[8]<=4:
									# {"feature": "Restaurantlessthan20", "instances": 222, "metric_value": 0.8665, "depth": 9}
									if obj[17]>1.0:
										# {"feature": "Restaurant20to50", "instances": 203, "metric_value": 0.8357, "depth": 10}
										if obj[18]<=2.0:
											# {"feature": "Carryaway", "instances": 180, "metric_value": 0.8024, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Occupation", "instances": 90, "metric_value": 0.6752, "depth": 12}
												if obj[12]<=14:
													# {"feature": "Temperature", "instances": 80, "metric_value": 0.7219, "depth": 13}
													if obj[3]>30:
														# {"feature": "Maritalstatus", "instances": 71, "metric_value": 0.6868, "depth": 14}
														if obj[9]<=2:
															# {"feature": "Education", "instances": 69, "metric_value": 0.6981, "depth": 15}
															if obj[11]<=3:
																# {"feature": "Bar", "instances": 67, "metric_value": 0.7098, "depth": 16}
																if obj[14]<=1.0:
																	# {"feature": "Weather", "instances": 37, "metric_value": 0.6395, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Direction_same", "instances": 34, "metric_value": 0.6024, "depth": 18}
																		if obj[19]>0:
																			# {"feature": "Gender", "instances": 21, "metric_value": 0.7025, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Time", "instances": 15, "metric_value": 0.5665, "depth": 20}
																				if obj[4]<=1:
																					# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					elif obj[10]>0:
																						return 'True'
																					else: return 'True'
																				elif obj[4]>1:
																					return 'True'
																				else: return 'True'
																			elif obj[7]<=0:
																				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[4]>0:
																					# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					elif obj[10]>0:
																						return 'False'
																					else: return 'False'
																				elif obj[4]<=0:
																					return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[19]<=0:
																			# {"feature": "Time", "instances": 13, "metric_value": 0.3912, "depth": 19}
																			if obj[4]>0:
																				return 'True'
																			elif obj[4]<=0:
																				# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					elif obj[10]>0:
																						return 'True'
																					else: return 'True'
																				elif obj[7]<=0:
																					return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[2]>0:
																		# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[10]>0:
																			return 'True'
																		elif obj[10]<=0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[14]>1.0:
																	# {"feature": "Time", "instances": 30, "metric_value": 0.7838, "depth": 17}
																	if obj[4]<=1:
																		# {"feature": "Children", "instances": 26, "metric_value": 0.8404, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Weather", "instances": 21, "metric_value": 0.7025, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Gender", "instances": 19, "metric_value": 0.7425, "depth": 20}
																				if obj[7]<=0:
																					# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 21}
																					if obj[19]>0:
																						return 'True'
																					elif obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[7]>0:
																					# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					elif obj[19]>0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[2]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[10]>0:
																			# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[7]<=0:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	elif obj[4]>1:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[11]>3:
																return 'True'
															else: return 'True'
														elif obj[9]>2:
															return 'True'
														else: return 'True'
													elif obj[3]<=30:
														# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[14]<=2.0:
															# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 15}
															if obj[7]>0:
																# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[2]>0:
																	# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[11]<=2:
																		return 'True'
																	elif obj[11]>2:
																		# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[4]<=1:
																			# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[2]<=0:
																	return 'False'
																else: return 'False'
															elif obj[7]<=0:
																return 'True'
															else: return 'True'
														elif obj[14]>2.0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[12]>14:
													return 'True'
												else: return 'True'
											elif obj[16]<=2.0:
												# {"feature": "Temperature", "instances": 90, "metric_value": 0.8945, "depth": 12}
												if obj[3]>30:
													# {"feature": "Occupation", "instances": 78, "metric_value": 0.9306, "depth": 13}
													if obj[12]>1:
														# {"feature": "Time", "instances": 69, "metric_value": 0.8865, "depth": 14}
														if obj[4]<=1:
															# {"feature": "Maritalstatus", "instances": 61, "metric_value": 0.9288, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Education", "instances": 37, "metric_value": 0.8419, "depth": 16}
																if obj[11]>1:
																	# {"feature": "Direction_same", "instances": 26, "metric_value": 0.7063, "depth": 17}
																	if obj[19]<=0:
																		# {"feature": "Gender", "instances": 17, "metric_value": 0.3228, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Bar", "instances": 10, "metric_value": 0.469, "depth": 19}
																			if obj[14]<=1.0:
																				# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[10]>0:
																					return 'True'
																				else: return 'True'
																			elif obj[14]>1.0:
																				return 'True'
																			else: return 'True'
																		elif obj[7]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[19]>0:
																		# {"feature": "Gender", "instances": 9, "metric_value": 0.9911, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Bar", "instances": 8, "metric_value": 0.9544, "depth": 19}
																			if obj[14]>-1.0:
																				# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[10]>0:
																					return 'True'
																				else: return 'True'
																			elif obj[14]<=-1.0:
																				return 'False'
																			else: return 'False'
																		elif obj[7]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[11]<=1:
																	# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 17}
																	if obj[14]<=1.0:
																		# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 18}
																		if obj[19]<=0:
																			# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[10]>0:
																						return 'False'
																					elif obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[7]<=0:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'False'
																					elif obj[10]>0:
																						return 'True'
																					else: return 'True'
																				else: return 'False'
																			elif obj[2]>0:
																				return 'False'
																			else: return 'False'
																		elif obj[19]>0:
																			return 'True'
																		else: return 'True'
																	elif obj[14]>1.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[9]>1:
																# {"feature": "Direction_same", "instances": 24, "metric_value": 0.995, "depth": 16}
																if obj[19]>0:
																	# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 17}
																	if obj[14]>0.0:
																		# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[11]>1:
																						return 'True'
																					elif obj[11]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'True'
																			elif obj[10]>0:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[11]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[11]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[14]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[19]<=0:
																	# {"feature": "Bar", "instances": 10, "metric_value": 0.8813, "depth": 17}
																	if obj[14]>0.0:
																		# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[11]>0:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[10]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[11]<=0:
																				return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[11]<=0:
																				return 'False'
																			elif obj[11]>0:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	elif obj[14]<=0.0:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[4]>1:
															return 'True'
														else: return 'True'
													elif obj[12]<=1:
														# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9183, "depth": 14}
														if obj[9]<=0:
															# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 15}
															if obj[11]>0:
																return 'True'
															elif obj[11]<=0:
																return 'False'
															else: return 'False'
														elif obj[9]>0:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[3]<=30:
													# {"feature": "Gender", "instances": 12, "metric_value": 0.4138, "depth": 13}
													if obj[7]>0:
														return 'True'
													elif obj[7]<=0:
														# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[11]>0:
															return 'True'
														elif obj[11]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[18]>2.0:
											# {"feature": "Gender", "instances": 23, "metric_value": 0.9877, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.65, "depth": 12}
												if obj[9]<=0:
													# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[12]>5:
														# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[11]<=1:
																return 'True'
															elif obj[11]>1:
																return 'False'
															else: return 'False'
														elif obj[3]>55:
															return 'True'
														else: return 'True'
													elif obj[12]<=5:
														return 'False'
													else: return 'False'
												elif obj[9]>0:
													return 'True'
												else: return 'True'
											elif obj[7]>0:
												# {"feature": "Bar", "instances": 11, "metric_value": 0.8454, "depth": 12}
												if obj[14]<=2.0:
													# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[4]>0:
														# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[9]<=2:
															return 'False'
														elif obj[9]>2:
															return 'True'
														else: return 'True'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[14]>2.0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[17]<=1.0:
										# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 10}
										if obj[11]<=3:
											# {"feature": "Bar", "instances": 17, "metric_value": 0.9774, "depth": 11}
											if obj[14]>0.0:
												# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 12}
												if obj[18]<=0.0:
													# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 13}
													if obj[9]>1:
														# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[4]>0:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=0:
																return 'True'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[4]<=0:
															return 'False'
														else: return 'False'
													elif obj[9]<=1:
														return 'True'
													else: return 'True'
												elif obj[18]>0.0:
													return 'False'
												else: return 'False'
											elif obj[14]<=0.0:
												# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 12}
												if obj[10]<=0:
													# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[3]>55:
														# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[4]<=0:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=0:
																return 'True'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[4]>0:
															return 'True'
														else: return 'True'
													elif obj[3]<=55:
														return 'False'
													else: return 'False'
												elif obj[10]>0:
													return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[11]>3:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>4:
									# {"feature": "Education", "instances": 49, "metric_value": 0.5364, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Carryaway", "instances": 43, "metric_value": 0.3651, "depth": 10}
										if obj[16]>1.0:
											# {"feature": "Occupation", "instances": 35, "metric_value": 0.1872, "depth": 11}
											if obj[12]>2:
												return 'True'
											elif obj[12]<=2:
												# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[4]>0:
													return 'True'
												elif obj[4]<=0:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=30:
														return 'True'
													elif obj[3]>30:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'True'
										elif obj[16]<=1.0:
											# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[4]>0:
													# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[2]<=0:
														return 'True'
													elif obj[2]>0:
														# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]>30:
															return 'False'
														elif obj[3]<=30:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											elif obj[9]>1:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Maritalstatus", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[2]<=0:
												return 'True'
											elif obj[2]>0:
												# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=30:
													return 'True'
												elif obj[3]>30:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[9]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=0:
								# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 8}
								if obj[8]<=5:
									# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 9}
									if obj[11]<=3:
										# {"feature": "Carryaway", "instances": 13, "metric_value": 0.8905, "depth": 10}
										if obj[16]>2.0:
											# {"feature": "Temperature", "instances": 8, "metric_value": 1.0, "depth": 11}
											if obj[3]>30:
												# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[12]<=4:
														return 'False'
													elif obj[12]>4:
														return 'True'
													else: return 'True'
												elif obj[2]>0:
													return 'False'
												else: return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[16]<=2.0:
											return 'True'
										else: return 'True'
									elif obj[11]>3:
										return 'False'
									else: return 'False'
								elif obj[8]>5:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[13]>5:
							# {"feature": "Occupation", "instances": 115, "metric_value": 0.6044, "depth": 7}
							if obj[12]>6:
								# {"feature": "Weather", "instances": 62, "metric_value": 0.7982, "depth": 8}
								if obj[2]<=1:
									# {"feature": "Gender", "instances": 61, "metric_value": 0.7772, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Temperature", "instances": 38, "metric_value": 0.6292, "depth": 10}
										if obj[3]>55:
											# {"feature": "Time", "instances": 29, "metric_value": 0.7355, "depth": 11}
											if obj[4]<=1:
												# {"feature": "Carryaway", "instances": 24, "metric_value": 0.8113, "depth": 12}
												if obj[16]>-1.0:
													# {"feature": "Bar", "instances": 22, "metric_value": 0.8454, "depth": 13}
													if obj[14]<=1.0:
														# {"feature": "Age", "instances": 15, "metric_value": 0.9183, "depth": 14}
														if obj[8]<=6:
															# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.9612, "depth": 15}
															if obj[9]>0:
																# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 16}
																if obj[19]>0:
																	return 'True'
																elif obj[19]<=0:
																	# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[18]>0.0:
																		# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[11]>0:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[17]<=3.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[11]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[18]<=0.0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[9]<=0:
																# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[1]>0:
																	# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[11]<=2:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=1.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[11]>2:
																			return 'False'
																		else: return 'False'
																	elif obj[10]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[8]>6:
															return 'True'
														else: return 'True'
													elif obj[14]>1.0:
														# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[8]<=5:
															return 'True'
														elif obj[8]>5:
															# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[19]>0:
																# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=1:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[11]<=0:
																				# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=1.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=2.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[19]<=0:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[16]<=-1.0:
													return 'True'
												else: return 'True'
											elif obj[4]>1:
												return 'True'
											else: return 'True'
										elif obj[3]<=55:
											return 'True'
										else: return 'True'
									elif obj[7]>0:
										# {"feature": "Age", "instances": 23, "metric_value": 0.9321, "depth": 10}
										if obj[8]<=5:
											# {"feature": "Children", "instances": 22, "metric_value": 0.9024, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Bar", "instances": 19, "metric_value": 0.9495, "depth": 12}
												if obj[14]<=2.0:
													# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 13}
													if obj[4]<=1:
														# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 14}
														if obj[19]<=0:
															# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[9]>0:
																# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[18]>1.0:
																	# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[3]<=55:
																		return 'False'
																	elif obj[3]>55:
																		return 'True'
																	else: return 'True'
																elif obj[18]<=1.0:
																	return 'True'
																else: return 'True'
															elif obj[9]<=0:
																return 'False'
															else: return 'False'
														elif obj[19]>0:
															# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[9]<=0:
																return 'True'
															elif obj[9]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[4]>1:
														return 'False'
													else: return 'False'
												elif obj[14]>2.0:
													# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[17]>1.0:
														return 'True'
													elif obj[17]<=1.0:
														# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[4]>0:
															return 'False'
														elif obj[4]<=0:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											elif obj[10]>0:
												return 'True'
											else: return 'True'
										elif obj[8]>5:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[2]>1:
									return 'False'
								else: return 'False'
							elif obj[12]<=6:
								# {"feature": "Bar", "instances": 53, "metric_value": 0.2318, "depth": 8}
								if obj[14]<=1.0:
									return 'True'
								elif obj[14]>1.0:
									# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.469, "depth": 9}
									if obj[9]>0:
										return 'True'
									elif obj[9]<=0:
										# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[19]>0:
											return 'True'
										elif obj[19]<=0:
											# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[3]>30:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7]>0:
													return 'True'
												elif obj[7]<=0:
													return 'False'
												else: return 'False'
											elif obj[3]<=30:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[20]>1:
						# {"feature": "Carryaway", "instances": 218, "metric_value": 0.9519, "depth": 6}
						if obj[16]>1.0:
							# {"feature": "Bar", "instances": 171, "metric_value": 0.9123, "depth": 7}
							if obj[14]>0.0:
								# {"feature": "Gender", "instances": 119, "metric_value": 0.9567, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Time", "instances": 62, "metric_value": 0.8474, "depth": 9}
									if obj[4]<=1:
										# {"feature": "Temperature", "instances": 56, "metric_value": 0.8856, "depth": 10}
										if obj[3]<=55:
											# {"feature": "Occupation", "instances": 40, "metric_value": 0.9544, "depth": 11}
											if obj[12]<=7:
												# {"feature": "Maritalstatus", "instances": 23, "metric_value": 0.8281, "depth": 12}
												if obj[9]>0:
													# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 13}
													if obj[13]<=3:
														# {"feature": "Weather", "instances": 11, "metric_value": 0.684, "depth": 14}
														if obj[2]<=0:
															# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[1]>0:
																# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[8]<=5:
																	# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[17]<=2.0:
																		return 'True'
																	elif obj[17]>2.0:
																		return 'False'
																	else: return 'False'
																elif obj[8]>5:
																	return 'False'
																else: return 'False'
															elif obj[1]<=0:
																return 'True'
															else: return 'True'
														elif obj[2]>0:
															return 'True'
														else: return 'True'
													elif obj[13]>3:
														# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[17]<=2.0:
															return 'False'
														elif obj[17]>2.0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[9]<=0:
													return 'True'
												else: return 'True'
											elif obj[12]>7:
												# {"feature": "Passanger", "instances": 17, "metric_value": 0.9975, "depth": 12}
												if obj[1]>0:
													# {"feature": "Income", "instances": 16, "metric_value": 0.9887, "depth": 13}
													if obj[13]<=1:
														# {"feature": "Children", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[17]>2.0:
																return 'False'
															elif obj[17]<=2.0:
																# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[19]<=0:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[8]<=1:
																			# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=2:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=1.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[19]>0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[10]>0:
															return 'True'
														else: return 'True'
													elif obj[13]>1:
														# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[17]<=2.0:
															# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[8]>0:
																# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[11]<=1:
																	return 'True'
																elif obj[11]>1:
																	return 'False'
																else: return 'False'
															elif obj[8]<=0:
																return 'False'
															else: return 'False'
														elif obj[17]>2.0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[3]>55:
											# {"feature": "Age", "instances": 16, "metric_value": 0.5436, "depth": 11}
											if obj[8]>3:
												# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 12}
												if obj[19]<=0:
													# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[9]>1:
														# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[18]>0.0:
															# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[10]>0:
																return 'True'
															elif obj[10]<=0:
																return 'False'
															else: return 'False'
														elif obj[18]<=0.0:
															return 'True'
														else: return 'True'
													elif obj[9]<=1:
														return 'True'
													else: return 'True'
												elif obj[19]>0:
													return 'False'
												else: return 'False'
											elif obj[8]<=3:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]>1:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									# {"feature": "Age", "instances": 57, "metric_value": 0.9998, "depth": 9}
									if obj[8]<=4:
										# {"feature": "Restaurantlessthan20", "instances": 50, "metric_value": 0.9896, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Restaurant20to50", "instances": 48, "metric_value": 0.9799, "depth": 11}
											if obj[18]<=3.0:
												# {"feature": "Education", "instances": 46, "metric_value": 0.9656, "depth": 12}
												if obj[11]<=2:
													# {"feature": "Income", "instances": 31, "metric_value": 0.8691, "depth": 13}
													if obj[13]<=4:
														# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 14}
														if obj[12]<=5:
															# {"feature": "Children", "instances": 10, "metric_value": 0.971, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[4]<=0:
																		return 'False'
																	elif obj[4]>0:
																		return 'True'
																	else: return 'True'
																elif obj[9]>0:
																	return 'True'
																else: return 'True'
															elif obj[10]>0:
																return 'False'
															else: return 'False'
														elif obj[12]>5:
															# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[2]<=0:
																		return 'True'
																	elif obj[2]>0:
																		# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[1]<=1:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=30:
																				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[4]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[9]>0:
																	return 'False'
																else: return 'False'
															elif obj[10]>0:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[13]>4:
														# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 14}
														if obj[12]>1:
															return 'True'
														elif obj[12]<=1:
															# {"feature": "Temperature", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[3]>55:
																return 'True'
															elif obj[3]<=55:
																# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[1]>0:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]>0:
																		return 'False'
																	elif obj[9]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[11]>2:
													# {"feature": "Income", "instances": 15, "metric_value": 0.971, "depth": 13}
													if obj[13]>0:
														# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.9957, "depth": 14}
														if obj[9]<=2:
															# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 15}
															if obj[4]<=1:
																# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 16}
																if obj[12]>1:
																	# {"feature": "Weather", "instances": 8, "metric_value": 1.0, "depth": 17}
																	if obj[2]>0:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[3]<=30:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[2]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[12]<=1:
																	return 'False'
																else: return 'False'
															elif obj[4]>1:
																return 'True'
															else: return 'True'
														elif obj[9]>2:
															return 'False'
														else: return 'False'
													elif obj[13]<=0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[18]>3.0:
												return 'False'
											else: return 'False'
										elif obj[17]<=1.0:
											return 'False'
										else: return 'False'
									elif obj[8]>4:
										# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[4]<=1:
											return 'False'
										elif obj[4]>1:
											# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[2]>0:
												return 'True'
											elif obj[2]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[14]<=0.0:
								# {"feature": "Income", "instances": 52, "metric_value": 0.7444, "depth": 8}
								if obj[13]>2:
									# {"feature": "Restaurantlessthan20", "instances": 40, "metric_value": 0.8485, "depth": 9}
									if obj[17]<=2.0:
										# {"feature": "Age", "instances": 22, "metric_value": 0.5746, "depth": 10}
										if obj[8]<=6:
											# {"feature": "Time", "instances": 19, "metric_value": 0.2975, "depth": 11}
											if obj[4]>0:
												return 'True'
											elif obj[4]<=0:
												# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[10]<=0:
													return 'True'
												elif obj[10]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>6:
											# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=55:
												return 'False'
											elif obj[3]>55:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[17]>2.0:
										# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Occupation", "instances": 17, "metric_value": 0.9774, "depth": 11}
											if obj[12]<=19:
												# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9544, "depth": 12}
												if obj[19]<=0:
													# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[18]>0.0:
														# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 14}
														if obj[9]<=2:
															return 'True'
														elif obj[9]>2:
															return 'False'
														else: return 'False'
													elif obj[18]<=0.0:
														# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[11]<=2:
															return 'False'
														elif obj[11]>2:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[19]>0:
													# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[8]>4:
														# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[7]>0:
															# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9]>2:
																return 'True'
															elif obj[9]<=2:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													elif obj[8]<=4:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[12]>19:
												return 'False'
											else: return 'False'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[13]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[16]<=1.0:
							# {"feature": "Direction_same", "instances": 47, "metric_value": 0.9971, "depth": 7}
							if obj[19]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 39, "metric_value": 0.9766, "depth": 8}
								if obj[17]<=2.0:
									# {"feature": "Education", "instances": 31, "metric_value": 0.9072, "depth": 9}
									if obj[11]<=3:
										# {"feature": "Age", "instances": 27, "metric_value": 0.8256, "depth": 10}
										if obj[8]<=4:
											# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 11}
											if obj[12]<=11:
												# {"feature": "Time", "instances": 19, "metric_value": 0.7425, "depth": 12}
												if obj[4]>0:
													# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.8905, "depth": 13}
													if obj[9]<=1:
														# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[18]<=1.0:
																	# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[2]>0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[13]<=8:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[2]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[13]<=5:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=2.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[18]>1.0:
																	return 'False'
																else: return 'False'
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[3]>55:
															return 'True'
														else: return 'True'
													elif obj[9]>1:
														return 'False'
													else: return 'False'
												elif obj[4]<=0:
													return 'False'
												else: return 'False'
											elif obj[12]>11:
												# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[13]>0:
													return 'True'
												elif obj[13]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[8]>4:
											return 'False'
										else: return 'False'
									elif obj[11]>3:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]>30:
											return 'True'
										elif obj[3]<=30:
											# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[2]<=0:
												return 'False'
											elif obj[2]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[17]>2.0:
									# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[12]<=7:
										return 'True'
									elif obj[12]>7:
										# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]<=55:
											return 'False'
										elif obj[3]>55:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[19]>0:
								# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[12]<=6:
									# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[13]<=7:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]<=0:
											return 'False'
										elif obj[7]>0:
											return 'True'
										else: return 'True'
									elif obj[13]>7:
										return 'True'
									else: return 'True'
								elif obj[12]>6:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[15]<=0.0:
				# {"feature": "Weather", "instances": 460, "metric_value": 0.977, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Income", "instances": 365, "metric_value": 0.9567, "depth": 5}
					if obj[13]>3:
						# {"feature": "Temperature", "instances": 214, "metric_value": 0.9893, "depth": 6}
						if obj[3]>30:
							# {"feature": "Distance", "instances": 196, "metric_value": 0.9981, "depth": 7}
							if obj[20]<=2:
								# {"feature": "Restaurantlessthan20", "instances": 181, "metric_value": 1.0, "depth": 8}
								if obj[17]>-1.0:
									# {"feature": "Carryaway", "instances": 177, "metric_value": 0.9994, "depth": 9}
									if obj[16]>1.0:
										# {"feature": "Occupation", "instances": 140, "metric_value": 0.9928, "depth": 10}
										if obj[12]<=7:
											# {"feature": "Age", "instances": 96, "metric_value": 0.9618, "depth": 11}
											if obj[8]>0:
												# {"feature": "Gender", "instances": 81, "metric_value": 0.9301, "depth": 12}
												if obj[7]>0:
													# {"feature": "Direction_same", "instances": 50, "metric_value": 0.9815, "depth": 13}
													if obj[19]<=0:
														# {"feature": "Time", "instances": 38, "metric_value": 0.9268, "depth": 14}
														if obj[4]>0:
															# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.8256, "depth": 15}
															if obj[18]>0.0:
																# {"feature": "Passanger", "instances": 17, "metric_value": 0.9367, "depth": 16}
																if obj[1]<=2:
																	# {"feature": "Maritalstatus", "instances": 10, "metric_value": 1.0, "depth": 17}
																	if obj[9]>0:
																		# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 18}
																		if obj[0]<=0:
																			# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[11]<=1:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=0.0:
																						return 'True'
																					else: return 'True'
																				elif obj[11]>1:
																					return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				return 'False'
																			else: return 'False'
																		elif obj[0]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[9]<=0:
																		# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[0]<=0:
																			# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[14]>0.0:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[11]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[14]<=0.0:
																				return 'True'
																			else: return 'True'
																		elif obj[0]>0:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[1]>2:
																	# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 17}
																	if obj[9]>0:
																		# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[11]<=0:
																				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[0]<=0:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=0.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[11]>0:
																				return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[9]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[18]<=0.0:
																# {"feature": "Children", "instances": 10, "metric_value": 0.469, "depth": 16}
																if obj[10]<=0:
																	return 'False'
																elif obj[10]>0:
																	# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[1]<=2:
																		# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[0]<=0:
																			# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=0:
																				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=0:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=0.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[1]>2:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[4]<=0:
															# {"feature": "Driving_to", "instances": 11, "metric_value": 0.994, "depth": 15}
															if obj[0]>0:
																# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[9]<=2:
																	return 'False'
																elif obj[9]>2:
																	return 'True'
																else: return 'True'
															elif obj[0]<=0:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[19]>0:
														# {"feature": "Time", "instances": 12, "metric_value": 0.9183, "depth": 14}
														if obj[4]>0:
															return 'True'
														elif obj[4]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[7]<=0:
													# {"feature": "Driving_to", "instances": 31, "metric_value": 0.7706, "depth": 13}
													if obj[0]<=1:
														# {"feature": "Time", "instances": 25, "metric_value": 0.8555, "depth": 14}
														if obj[4]>0:
															# {"feature": "Maritalstatus", "instances": 20, "metric_value": 0.6098, "depth": 15}
															if obj[9]<=1:
																# {"feature": "Education", "instances": 16, "metric_value": 0.3373, "depth": 16}
																if obj[11]<=2:
																	return 'False'
																elif obj[11]>2:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]>1:
																		return 'False'
																	elif obj[1]<=1:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[9]>1:
																# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[19]<=0:
																	# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[1]>1:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[11]<=2:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=1.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[1]<=1:
																		return 'False'
																	else: return 'False'
																elif obj[19]>0:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[4]<=0:
															# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[9]<=1:
																return 'True'
															elif obj[9]>1:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[0]>1:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]<=0:
												# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 12}
												if obj[11]>0:
													# {"feature": "Time", "instances": 13, "metric_value": 0.8905, "depth": 13}
													if obj[4]<=2:
														# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[7]<=0:
															# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 15}
															if obj[18]<=0.0:
																# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[0]<=1:
																	# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[19]<=0:
																		# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[1]>1:
																			# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[9]<=1:
																				# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[14]<=1.0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[1]<=1:
																			return 'False'
																		else: return 'False'
																	elif obj[19]>0:
																		return 'True'
																	else: return 'True'
																elif obj[0]>1:
																	return 'False'
																else: return 'False'
															elif obj[18]>0.0:
																return 'True'
															else: return 'True'
														elif obj[7]>0:
															return 'True'
														else: return 'True'
													elif obj[4]>2:
														return 'True'
													else: return 'True'
												elif obj[11]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[12]>7:
											# {"feature": "Education", "instances": 44, "metric_value": 0.976, "depth": 11}
											if obj[11]>0:
												# {"feature": "Bar", "instances": 28, "metric_value": 0.9963, "depth": 12}
												if obj[14]<=1.0:
													# {"feature": "Passanger", "instances": 17, "metric_value": 0.9774, "depth": 13}
													if obj[1]>1:
														# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 14}
														if obj[4]<=2:
															# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 15}
															if obj[8]>0:
																# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[0]<=0:
																		# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[9]>0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[9]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
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
																elif obj[7]<=0:
																	# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[0]<=0:
																		# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
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
															elif obj[8]<=0:
																# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[0]<=0:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[9]<=0:
																			# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[18]<=3.0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[4]>2:
															return 'False'
														else: return 'False'
													elif obj[1]<=1:
														# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[9]<=0:
															return 'True'
														elif obj[9]>0:
															# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[0]<=0:
																return 'True'
															elif obj[0]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[14]>1.0:
													# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 13}
													if obj[18]<=1.0:
														# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[4]<=2:
															# {"feature": "Driving_to", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[0]<=1:
																# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 16}
																if obj[1]>1:
																	# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[8]<=0:
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
																	elif obj[8]>0:
																		return 'False'
																	else: return 'False'
																elif obj[1]<=1:
																	# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[8]>0:
																		return 'True'
																	elif obj[8]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[0]>1:
																return 'False'
															else: return 'False'
														elif obj[4]>2:
															return 'True'
														else: return 'True'
													elif obj[18]>1.0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[11]<=0:
												# {"feature": "Age", "instances": 16, "metric_value": 0.6962, "depth": 12}
												if obj[8]>1:
													# {"feature": "Passanger", "instances": 14, "metric_value": 0.7496, "depth": 13}
													if obj[1]<=1:
														# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 14}
														if obj[4]<=3:
															# {"feature": "Driving_to", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[0]>1:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]>0:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=1:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=2.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=2.0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[7]<=0:
																	return 'True'
																else: return 'True'
															elif obj[0]<=1:
																return 'True'
															else: return 'True'
														elif obj[4]>3:
															return 'False'
														else: return 'False'
													elif obj[1]>1:
														# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 14}
														if obj[7]>0:
															# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[0]<=0:
																# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[4]<=2:
																	# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[9]<=0:
																		# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[10]<=1:
																			# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[14]<=0.0:
																				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[18]<=1.0:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[8]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[16]<=1.0:
										# {"feature": "Occupation", "instances": 37, "metric_value": 0.9569, "depth": 10}
										if obj[12]<=10:
											# {"feature": "Age", "instances": 20, "metric_value": 0.7219, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 12}
												if obj[11]>1:
													# {"feature": "Driving_to", "instances": 8, "metric_value": 0.5436, "depth": 13}
													if obj[0]<=1:
														return 'True'
													elif obj[0]>1:
														return 'False'
													else: return 'False'
												elif obj[11]<=1:
													# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[0]<=0:
														# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[1]>1:
															# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[4]<=2:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]<=4:
																		# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[14]<=0.0:
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
															elif obj[7]>0:
																return 'False'
															else: return 'False'
														elif obj[1]<=1:
															return 'True'
														else: return 'True'
													elif obj[0]>0:
														return 'False'
													else: return 'False'
												else: return 'False'
											elif obj[8]>4:
												return 'True'
											else: return 'True'
										elif obj[12]>10:
											# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 11}
											if obj[11]>1:
												# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 12}
												if obj[4]<=2:
													# {"feature": "Driving_to", "instances": 10, "metric_value": 1.0, "depth": 13}
													if obj[0]>0:
														# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[8]<=4:
															# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[19]<=0:
																return 'True'
															elif obj[19]>0:
																# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[14]<=0.0:
																					# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[18]<=-1.0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[9]>0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[8]>4:
															return 'False'
														else: return 'False'
													elif obj[0]<=0:
														# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8]<=0:
															return 'False'
														elif obj[8]>0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[4]>2:
													return 'True'
												else: return 'True'
											elif obj[11]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[17]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[20]>2:
								# {"feature": "Gender", "instances": 15, "metric_value": 0.5665, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[11]>2:
										return 'True'
									elif obj[11]<=2:
										# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=30:
							# {"feature": "Occupation", "instances": 18, "metric_value": 0.3095, "depth": 7}
							if obj[12]<=18:
								return 'True'
							elif obj[12]>18:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[13]<=3:
						# {"feature": "Age", "instances": 151, "metric_value": 0.8705, "depth": 6}
						if obj[8]<=5:
							# {"feature": "Occupation", "instances": 122, "metric_value": 0.8177, "depth": 7}
							if obj[12]<=11:
								# {"feature": "Bar", "instances": 98, "metric_value": 0.73, "depth": 8}
								if obj[14]<=2.0:
									# {"feature": "Driving_to", "instances": 83, "metric_value": 0.6547, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Maritalstatus", "instances": 61, "metric_value": 0.5141, "depth": 10}
										if obj[9]>0:
											# {"feature": "Distance", "instances": 52, "metric_value": 0.57, "depth": 11}
											if obj[20]<=2:
												# {"feature": "Direction_same", "instances": 44, "metric_value": 0.6321, "depth": 12}
												if obj[19]<=0:
													# {"feature": "Time", "instances": 38, "metric_value": 0.6892, "depth": 13}
													if obj[4]>0:
														# {"feature": "Education", "instances": 34, "metric_value": 0.7335, "depth": 14}
														if obj[11]<=3:
															# {"feature": "Restaurant20to50", "instances": 31, "metric_value": 0.7706, "depth": 15}
															if obj[18]>0.0:
																# {"feature": "Passanger", "instances": 24, "metric_value": 0.65, "depth": 16}
																if obj[1]>2:
																	# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.8905, "depth": 17}
																	if obj[17]<=2.0:
																		# {"feature": "Temperature", "instances": 10, "metric_value": 0.7219, "depth": 18}
																		if obj[3]>55:
																			# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 19}
																			if obj[16]<=2.0:
																				# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[7]<=0:
																					# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[10]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[16]>2.0:
																				return 'True'
																			else: return 'True'
																		elif obj[3]<=55:
																			return 'True'
																		else: return 'True'
																	elif obj[17]>2.0:
																		# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[3]<=55:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				return 'False'
																			elif obj[10]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[3]>55:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[1]<=2:
																	return 'True'
																else: return 'True'
															elif obj[18]<=0.0:
																# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[3]<=55:
																			return 'True'
																		elif obj[3]>55:
																			return 'False'
																		else: return 'False'
																	elif obj[10]>0:
																		return 'False'
																	else: return 'False'
																elif obj[1]>1:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[11]>3:
															return 'True'
														else: return 'True'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[19]>0:
													return 'True'
												else: return 'True'
											elif obj[20]>2:
												return 'True'
											else: return 'True'
										elif obj[9]<=0:
											return 'True'
										else: return 'True'
									elif obj[0]>1:
										# {"feature": "Gender", "instances": 22, "metric_value": 0.9024, "depth": 10}
										if obj[7]>0:
											# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 11}
											if obj[4]<=0:
												# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 12}
												if obj[3]>30:
													# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.65, "depth": 13}
													if obj[9]>0:
														return 'False'
													elif obj[9]<=0:
														return 'True'
													else: return 'True'
												elif obj[3]<=30:
													return 'True'
												else: return 'True'
											elif obj[4]>0:
												# {"feature": "Carryaway", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[16]>1.0:
													return 'True'
												elif obj[16]<=1.0:
													# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=2:
														return 'False'
													elif obj[11]>2:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[7]<=0:
											# {"feature": "Temperature", "instances": 10, "metric_value": 0.469, "depth": 11}
											if obj[3]>30:
												return 'True'
											elif obj[3]<=30:
												# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[16]>2.0:
													return 'True'
												elif obj[16]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[14]>2.0:
									# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 9}
									if obj[4]<=1:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[1]>0:
											# {"feature": "Driving_to", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[0]>0:
												return 'True'
											elif obj[0]<=0:
												# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[11]>0:
													return 'True'
												elif obj[11]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[1]<=0:
											return 'False'
										else: return 'False'
									elif obj[4]>1:
										# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[9]>0:
											# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[3]>30:
												return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[9]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'True'
							elif obj[12]>11:
								# {"feature": "Carryaway", "instances": 24, "metric_value": 0.995, "depth": 8}
								if obj[16]>1.0:
									# {"feature": "Children", "instances": 18, "metric_value": 0.9183, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 10}
										if obj[4]>0:
											# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[0]<=1:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[19]<=0:
													return 'True'
												elif obj[19]>0:
													# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=1:
														# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3]<=80:
															# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7]<=1:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=2:
																	# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[11]<=2:
																		# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14]<=1.0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[17]<=1.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[18]<=0.0:
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
											elif obj[0]>1:
												return 'False'
											else: return 'False'
										elif obj[4]<=0:
											return 'True'
										else: return 'True'
									elif obj[10]>0:
										# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[4]>1:
												return 'True'
											elif obj[4]<=1:
												# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[20]<=2:
													return 'False'
												elif obj[20]>2:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[1]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[16]<=1.0:
									# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[1]<=2:
											return 'False'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[8]>5:
							# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9923, "depth": 7}
							if obj[18]<=1.0:
								# {"feature": "Gender", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[7]>0:
									# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[4]<=2:
										# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[20]>1:
												return 'True'
											elif obj[20]<=1:
												# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9]>0:
													return 'False'
												elif obj[9]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									elif obj[4]>2:
										return 'True'
									else: return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[18]>1.0:
								# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[12]<=18:
										return 'True'
									elif obj[12]>18:
										return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[4]>0:
										# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[10]>0:
											return 'False'
										elif obj[10]<=0:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]>0:
					# {"feature": "Passanger", "instances": 95, "metric_value": 0.9961, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 65, "metric_value": 0.9233, "depth": 6}
						if obj[12]>1:
							# {"feature": "Bar", "instances": 55, "metric_value": 0.971, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.9968, "depth": 8}
								if obj[18]<=1.0:
									# {"feature": "Gender", "instances": 35, "metric_value": 0.9518, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Age", "instances": 19, "metric_value": 0.8315, "depth": 10}
										if obj[8]<=5:
											# {"feature": "Maritalstatus", "instances": 18, "metric_value": 0.7642, "depth": 11}
											if obj[9]<=1:
												# {"feature": "Carryaway", "instances": 14, "metric_value": 0.8631, "depth": 12}
												if obj[16]<=2.0:
													# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 13}
													if obj[13]>2:
														# {"feature": "Time", "instances": 10, "metric_value": 0.8813, "depth": 14}
														if obj[4]<=1:
															# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 15}
															if obj[10]<=0:
																return 'False'
															elif obj[10]>0:
																# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[11]<=0:
																	return 'False'
																elif obj[11]>0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[4]>1:
															# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[20]>1:
																return 'False'
															elif obj[20]<=1:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[13]<=2:
														return 'True'
													else: return 'True'
												elif obj[16]>2.0:
													return 'False'
												else: return 'False'
											elif obj[9]>1:
												return 'False'
											else: return 'False'
										elif obj[8]>5:
											return 'True'
										else: return 'True'
									elif obj[7]>0:
										# {"feature": "Distance", "instances": 16, "metric_value": 1.0, "depth": 10}
										if obj[20]>1:
											# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 11}
											if obj[11]>0:
												# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 12}
												if obj[13]>1:
													return 'False'
												elif obj[13]<=1:
													# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0]>0:
														return 'True'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[11]<=0:
												return 'True'
											else: return 'True'
										elif obj[20]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[18]>1.0:
									# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[8]<=3:
										# {"feature": "Driving_to", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Carryaway", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[16]<=2.0:
												# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[19]<=0:
													return 'True'
												elif obj[19]>0:
													# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9]<=0:
														return 'True'
													elif obj[9]>0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[16]>2.0:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[8]>3:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[14]>1.0:
								# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[18]>0.0:
									return 'False'
								elif obj[18]<=0.0:
									# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>1:
										return 'False'
									elif obj[0]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[12]<=1:
							return 'False'
						else: return 'False'
					elif obj[1]>1:
						# {"feature": "Bar", "instances": 30, "metric_value": 0.8366, "depth": 6}
						if obj[14]>0.0:
							# {"feature": "Income", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[13]<=4:
								# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[8]<=1:
									# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[4]>2:
											# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[9]>0:
												# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[0]<=0:
													# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[3]<=30:
														# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[11]>0:
																# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12]<=1:
																	# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=3.0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=2.0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=1.0:
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
															elif obj[11]<=0:
																# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12]<=10:
																	# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=4.0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=2.0:
																			# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[18]<=0.0:
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
														else: return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[4]<=2:
											return 'False'
										else: return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[8]>1:
									return 'False'
								else: return 'False'
							elif obj[13]>4:
								return 'True'
							else: return 'True'
						elif obj[14]<=0.0:
							# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 7}
							if obj[12]<=11:
								return 'True'
							elif obj[12]>11:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]<=3:
									return 'True'
								elif obj[4]>3:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Bar", "instances": 1422, "metric_value": 0.9776, "depth": 2}
		if obj[14]>0.0:
			# {"feature": "Weather", "instances": 834, "metric_value": 0.9985, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Coupon_validity", "instances": 735, "metric_value": 0.9917, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Time", "instances": 520, "metric_value": 0.9698, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Restaurant20to50", "instances": 325, "metric_value": 0.9263, "depth": 6}
						if obj[18]<=3.0:
							# {"feature": "Age", "instances": 315, "metric_value": 0.9362, "depth": 7}
							if obj[8]<=3:
								# {"feature": "Maritalstatus", "instances": 187, "metric_value": 0.9774, "depth": 8}
								if obj[9]<=1:
									# {"feature": "Income", "instances": 146, "metric_value": 0.9206, "depth": 9}
									if obj[13]<=3:
										# {"feature": "Passanger", "instances": 87, "metric_value": 0.9723, "depth": 10}
										if obj[1]>0:
											# {"feature": "Restaurantlessthan20", "instances": 80, "metric_value": 0.9887, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Occupation", "instances": 78, "metric_value": 0.9829, "depth": 12}
												if obj[12]<=9:
													# {"feature": "Carryaway", "instances": 44, "metric_value": 1.0, "depth": 13}
													if obj[16]>1.0:
														# {"feature": "Coffeehouse", "instances": 42, "metric_value": 0.9984, "depth": 14}
														if obj[15]<=3.0:
															# {"feature": "Distance", "instances": 34, "metric_value": 0.9975, "depth": 15}
															if obj[20]>1:
																# {"feature": "Temperature", "instances": 22, "metric_value": 0.994, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Children", "instances": 17, "metric_value": 0.9975, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Driving_to", "instances": 14, "metric_value": 0.9852, "depth": 18}
																		if obj[0]<=1:
																			# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 19}
																			if obj[7]>0:
																				# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=2:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					elif obj[19]>0:
																						return 'False'
																					else: return 'False'
																				else: return 'True'
																			elif obj[7]<=0:
																				return 'False'
																			else: return 'False'
																		elif obj[0]>1:
																			# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 19}
																			if obj[11]<=2:
																				# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[7]>0:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[7]<=0:
																					return 'False'
																				else: return 'False'
																			elif obj[11]>2:
																				return 'True'
																			else: return 'True'
																		else: return 'True'
																	elif obj[10]<=0:
																		# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[0]<=1:
																			return 'True'
																		elif obj[0]>1:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[3]>55:
																	# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[11]>0:
																				return 'True'
																			elif obj[11]<=0:
																				return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[20]<=1:
																# {"feature": "Driving_to", "instances": 12, "metric_value": 0.9183, "depth": 16}
																if obj[0]>1:
																	# {"feature": "Temperature", "instances": 8, "metric_value": 1.0, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 18}
																		if obj[7]>0:
																			# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[10]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[7]<=0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=1:
																				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[11]<=3:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=1:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[3]>55:
																		return 'False'
																	else: return 'False'
																elif obj[0]<=1:
																	return 'False'
																else: return 'False'
															else: return 'False'
														elif obj[15]>3.0:
															# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 15}
															if obj[11]<=2:
																return 'True'
															elif obj[11]>2:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[16]<=1.0:
														return 'False'
													else: return 'False'
												elif obj[12]>9:
													# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9082, "depth": 13}
													if obj[15]<=3.0:
														# {"feature": "Education", "instances": 32, "metric_value": 0.8571, "depth": 14}
														if obj[11]<=3:
															# {"feature": "Carryaway", "instances": 29, "metric_value": 0.7973, "depth": 15}
															if obj[16]>2.0:
																# {"feature": "Gender", "instances": 16, "metric_value": 0.6962, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Temperature", "instances": 10, "metric_value": 0.469, "depth": 17}
																	if obj[3]>30:
																		return 'True'
																	elif obj[3]<=30:
																		# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[0]<=2:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=1:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[0]<=1:
																		# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[10]>0:
																			# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=3:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[3]>55:
																				return 'False'
																			else: return 'False'
																		elif obj[10]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[0]>1:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[16]<=2.0:
																# {"feature": "Temperature", "instances": 13, "metric_value": 0.8905, "depth": 16}
																if obj[3]>30:
																	# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 17}
																	if obj[20]<=2:
																		# {"feature": "Children", "instances": 7, "metric_value": 0.9852, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[19]<=0:
																				return 'True'
																			elif obj[19]>0:
																				# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[0]<=2:
																					# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[7]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[10]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[20]>2:
																		# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[10]>0:
																			return 'True'
																		elif obj[10]<=0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[3]<=30:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[11]>3:
															# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[0]>0:
																return 'False'
															elif obj[0]<=0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[15]>3.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[17]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[13]>3:
										# {"feature": "Carryaway", "instances": 59, "metric_value": 0.7905, "depth": 10}
										if obj[16]<=3.0:
											# {"feature": "Education", "instances": 51, "metric_value": 0.714, "depth": 11}
											if obj[11]>1:
												# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.8338, "depth": 12}
												if obj[15]>1.0:
													# {"feature": "Restaurantlessthan20", "instances": 21, "metric_value": 0.9587, "depth": 13}
													if obj[17]<=2.0:
														# {"feature": "Temperature", "instances": 11, "metric_value": 0.994, "depth": 14}
														if obj[3]<=55:
															# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[12]<=5:
																# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[0]<=1:
																	return 'True'
																elif obj[0]>1:
																	# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[19]>0:
																		return 'True'
																	elif obj[19]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[12]>5:
																return 'False'
															else: return 'False'
														elif obj[3]>55:
															# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 15}
															if obj[12]<=5:
																return 'False'
															elif obj[12]>5:
																# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[0]<=0:
																	return 'False'
																elif obj[0]>0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														else: return 'False'
													elif obj[17]>2.0:
														# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 14}
														if obj[12]<=20:
															# {"feature": "Driving_to", "instances": 9, "metric_value": 0.5033, "depth": 15}
															if obj[0]>1:
																return 'True'
															elif obj[0]<=1:
																# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[3]>55:
																	# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[1]<=1:
																		# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[7]<=1:
																			# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[3]<=55:
																	return 'True'
																else: return 'True'
															else: return 'True'
														elif obj[12]>20:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[15]<=1.0:
													# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.3912, "depth": 13}
													if obj[17]<=2.0:
														return 'True'
													elif obj[17]>2.0:
														# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[0]>1:
															# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[19]>0:
																return 'True'
															elif obj[19]<=0:
																return 'False'
															else: return 'False'
														elif obj[0]<=1:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[11]<=1:
												# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.3228, "depth": 12}
												if obj[17]>1.0:
													return 'True'
												elif obj[17]<=1.0:
													# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[0]<=1:
														return 'True'
													elif obj[0]>1:
														# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10]<=0:
															return 'True'
														elif obj[10]>0:
															return 'False'
														else: return 'False'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										elif obj[16]>3.0:
											# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 11}
											if obj[12]>5:
												# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[0]>0:
													return 'True'
												elif obj[0]<=0:
													# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3]<=55:
														return 'False'
													elif obj[3]>55:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[12]<=5:
												# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[3]>55:
													return 'False'
												elif obj[3]<=55:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]<=0:
														return 'False'
													elif obj[7]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[9]>1:
									# {"feature": "Occupation", "instances": 41, "metric_value": 0.9012, "depth": 9}
									if obj[12]<=11:
										# {"feature": "Income", "instances": 24, "metric_value": 0.995, "depth": 10}
										if obj[13]>1:
											# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 11}
											if obj[11]>0:
												# {"feature": "Driving_to", "instances": 11, "metric_value": 0.8454, "depth": 12}
												if obj[0]<=1:
													# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[17]>1.0:
														# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[7]>0:
															# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[1]>0:
																# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[3]<=55:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]<=0:
																		return 'False'
																	elif obj[10]>0:
																		return 'True'
																	else: return 'True'
																elif obj[3]>55:
																	return 'False'
																else: return 'False'
															elif obj[1]<=0:
																return 'True'
															else: return 'True'
														elif obj[7]<=0:
															return 'False'
														else: return 'False'
													elif obj[17]<=1.0:
														return 'True'
													else: return 'True'
												elif obj[0]>1:
													return 'True'
												else: return 'True'
											elif obj[11]<=0:
												# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9183, "depth": 12}
												if obj[0]>0:
													# {"feature": "Restaurantlessthan20", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[17]<=1.0:
														# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[19]<=0:
															# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[20]>2:
																	return 'True'
																elif obj[20]<=2:
																	return 'False'
																else: return 'False'
															elif obj[10]>0:
																return 'False'
															else: return 'False'
														elif obj[19]>0:
															return 'True'
														else: return 'True'
													elif obj[17]>1.0:
														return 'False'
													else: return 'False'
												elif obj[0]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[13]<=1:
											return 'False'
										else: return 'False'
									elif obj[12]>11:
										# {"feature": "Income", "instances": 17, "metric_value": 0.5226, "depth": 10}
										if obj[13]>0:
											return 'False'
										elif obj[13]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[8]>3:
								# {"feature": "Passanger", "instances": 128, "metric_value": 0.8351, "depth": 8}
								if obj[1]>0:
									# {"feature": "Occupation", "instances": 117, "metric_value": 0.8695, "depth": 9}
									if obj[12]<=13:
										# {"feature": "Direction_same", "instances": 102, "metric_value": 0.9082, "depth": 10}
										if obj[19]<=0:
											# {"feature": "Income", "instances": 75, "metric_value": 0.9532, "depth": 11}
											if obj[13]<=4:
												# {"feature": "Maritalstatus", "instances": 46, "metric_value": 0.859, "depth": 12}
												if obj[9]>0:
													# {"feature": "Restaurantlessthan20", "instances": 37, "metric_value": 0.7532, "depth": 13}
													if obj[17]<=2.0:
														# {"feature": "Driving_to", "instances": 28, "metric_value": 0.8631, "depth": 14}
														if obj[0]<=1:
															# {"feature": "Gender", "instances": 18, "metric_value": 0.65, "depth": 15}
															if obj[7]<=0:
																# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 16}
																if obj[11]>0:
																	# {"feature": "Carryaway", "instances": 6, "metric_value": 0.65, "depth": 17}
																	if obj[16]<=2.0:
																		return 'True'
																	elif obj[16]>2.0:
																		# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[15]<=2.0:
																			return 'True'
																		elif obj[15]>2.0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																elif obj[11]<=0:
																	# {"feature": "Temperature", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[3]<=55:
																		# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[15]<=0.0:
																			# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[10]<=0:
																				# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[16]<=1.0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=3:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		elif obj[15]>0.0:
																			return 'True'
																		else: return 'True'
																	elif obj[3]>55:
																		# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[15]<=0.0:
																			return 'True'
																		elif obj[15]>0.0:
																			return 'False'
																		else: return 'False'
																	else: return 'True'
																else: return 'True'
															elif obj[7]>0:
																return 'True'
															else: return 'True'
														elif obj[0]>1:
															# {"feature": "Carryaway", "instances": 10, "metric_value": 1.0, "depth": 15}
															if obj[16]>1.0:
																# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[15]<=1.0:
																		return 'False'
																	elif obj[15]>1.0:
																		return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	return 'False'
																else: return 'False'
															elif obj[16]<=1.0:
																return 'True'
															else: return 'True'
														else: return 'False'
													elif obj[17]>2.0:
														return 'True'
													else: return 'True'
												elif obj[9]<=0:
													# {"feature": "Driving_to", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[0]>0:
														# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 14}
														if obj[11]<=2:
															# {"feature": "Temperature", "instances": 7, "metric_value": 0.9852, "depth": 15}
															if obj[3]<=55:
																# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[10]>0:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[16]>2.0:
																			return 'True'
																		elif obj[16]<=2.0:
																			return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		return 'True'
																	else: return 'True'
																elif obj[10]<=0:
																	return 'False'
																else: return 'False'
															elif obj[3]>55:
																# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[10]>0:
																	return 'False'
																elif obj[10]<=0:
																	return 'True'
																else: return 'True'
															else: return 'False'
														elif obj[11]>2:
															return 'False'
														else: return 'False'
													elif obj[0]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[13]>4:
												# {"feature": "Education", "instances": 29, "metric_value": 0.9991, "depth": 12}
												if obj[11]<=2:
													# {"feature": "Driving_to", "instances": 22, "metric_value": 0.976, "depth": 13}
													if obj[0]>0:
														# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.998, "depth": 14}
														if obj[17]>1.0:
															# {"feature": "Children", "instances": 17, "metric_value": 0.9975, "depth": 15}
															if obj[10]<=0:
																# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.9612, "depth": 16}
																if obj[9]<=1:
																	# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 17}
																	if obj[15]>0.0:
																		# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 18}
																		if obj[20]>2:
																			# {"feature": "Carryaway", "instances": 7, "metric_value": 0.9852, "depth": 19}
																			if obj[16]<=3.0:
																				# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 20}
																				if obj[7]>0:
																					return 'True'
																				elif obj[7]<=0:
																					# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[3]<=55:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[16]>3.0:
																				return 'False'
																			else: return 'False'
																		elif obj[20]<=2:
																			return 'False'
																		else: return 'False'
																	elif obj[15]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[9]>1:
																	return 'False'
																else: return 'False'
															elif obj[10]>0:
																return 'True'
															else: return 'True'
														elif obj[17]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												elif obj[11]>2:
													# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[15]>0.0:
														# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[17]<=1.0:
															# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[0]<=0:
																return 'True'
															elif obj[0]>0:
																return 'False'
															else: return 'False'
														elif obj[17]>1.0:
															return 'True'
														else: return 'True'
													elif obj[15]<=0.0:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										elif obj[19]>0:
											# {"feature": "Restaurantlessthan20", "instances": 27, "metric_value": 0.6913, "depth": 11}
											if obj[17]<=2.0:
												# {"feature": "Coffeehouse", "instances": 19, "metric_value": 0.8315, "depth": 12}
												if obj[15]<=3.0:
													# {"feature": "Temperature", "instances": 18, "metric_value": 0.7642, "depth": 13}
													if obj[3]<=55:
														# {"feature": "Driving_to", "instances": 14, "metric_value": 0.5917, "depth": 14}
														if obj[0]>1:
															return 'True'
														elif obj[0]<=1:
															# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[13]>3:
																# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[16]>1.0:
																	return 'False'
																elif obj[16]<=1.0:
																	return 'True'
																else: return 'True'
															elif obj[13]<=3:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[3]>55:
														# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[7]>0:
															# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[10]>0:
																# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[11]>0:
																	return 'True'
																elif obj[11]<=0:
																	return 'False'
																else: return 'False'
															elif obj[10]<=0:
																return 'False'
															else: return 'False'
														elif obj[7]<=0:
															return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[15]>3.0:
													return 'False'
												else: return 'False'
											elif obj[17]>2.0:
												return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[12]>13:
										# {"feature": "Education", "instances": 15, "metric_value": 0.3534, "depth": 10}
										if obj[11]<=3:
											return 'True'
										elif obj[11]>3:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[18]>3.0:
							return 'True'
						else: return 'True'
					elif obj[4]>2:
						# {"feature": "Children", "instances": 195, "metric_value": 0.9998, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Driving_to", "instances": 131, "metric_value": 0.9644, "depth": 7}
							if obj[0]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 96, "metric_value": 0.8838, "depth": 8}
								if obj[17]>1.0:
									# {"feature": "Occupation", "instances": 79, "metric_value": 0.7959, "depth": 9}
									if obj[12]<=7:
										# {"feature": "Temperature", "instances": 46, "metric_value": 0.9109, "depth": 10}
										if obj[3]>55:
											# {"feature": "Carryaway", "instances": 29, "metric_value": 0.7973, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Age", "instances": 19, "metric_value": 0.9495, "depth": 12}
												if obj[8]<=4:
													# {"feature": "Passanger", "instances": 16, "metric_value": 0.8113, "depth": 13}
													if obj[1]>1:
														# {"feature": "Income", "instances": 9, "metric_value": 0.9911, "depth": 14}
														if obj[13]>0:
															# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 15}
															if obj[18]<=2.0:
																# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[20]>1:
																	return 'True'
																elif obj[20]<=1:
																	return 'False'
																else: return 'False'
															elif obj[18]>2.0:
																return 'False'
															else: return 'False'
														elif obj[13]<=0:
															return 'False'
														else: return 'False'
													elif obj[1]<=1:
														return 'True'
													else: return 'True'
												elif obj[8]>4:
													return 'False'
												else: return 'False'
											elif obj[16]<=2.0:
												return 'True'
											else: return 'True'
										elif obj[3]<=55:
											# {"feature": "Carryaway", "instances": 17, "metric_value": 0.9975, "depth": 11}
											if obj[16]>2.0:
												# {"feature": "Maritalstatus", "instances": 14, "metric_value": 0.9403, "depth": 12}
												if obj[9]<=0:
													# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[13]<=6:
														# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[18]>1.0:
															# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[15]>1.0:
																# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[1]<=0:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]>0:
																		return 'True'
																	elif obj[7]<=0:
																		return 'False'
																	else: return 'False'
																elif obj[1]>0:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]>0:
																		return 'False'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[15]<=1.0:
																return 'True'
															else: return 'True'
														elif obj[18]<=1.0:
															return 'False'
														else: return 'False'
													elif obj[13]>6:
														return 'False'
													else: return 'False'
												elif obj[9]>0:
													# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[11]<=2:
														return 'True'
													elif obj[11]>2:
														# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8]>1:
															return 'False'
														elif obj[8]<=1:
															return 'True'
														else: return 'True'
													else: return 'False'
												else: return 'True'
											elif obj[16]<=2.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[12]>7:
										# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.5328, "depth": 10}
										if obj[18]<=1.0:
											# {"feature": "Age", "instances": 17, "metric_value": 0.7871, "depth": 11}
											if obj[8]>0:
												# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.5665, "depth": 12}
												if obj[15]>1.0:
													return 'True'
												elif obj[15]<=1.0:
													# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[7]>0:
														# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[1]<=1:
															# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[3]>55:
																# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9]<=1:
																	return 'True'
																elif obj[9]>1:
																	return 'False'
																else: return 'False'
															elif obj[3]<=55:
																return 'True'
															else: return 'True'
														elif obj[1]>1:
															return 'False'
														else: return 'False'
													elif obj[7]<=0:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										elif obj[18]>1.0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[17]<=1.0:
									# {"feature": "Temperature", "instances": 17, "metric_value": 0.9774, "depth": 9}
									if obj[3]>55:
										# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[11]>0:
											# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[8]>0:
												# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 12}
												if obj[13]>2:
													return 'True'
												elif obj[13]<=2:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										elif obj[11]<=0:
											return 'False'
										else: return 'False'
									elif obj[3]<=55:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>0:
								# {"feature": "Age", "instances": 35, "metric_value": 0.9518, "depth": 8}
								if obj[8]>0:
									# {"feature": "Gender", "instances": 30, "metric_value": 0.8813, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9911, "depth": 10}
										if obj[18]<=2.0:
											# {"feature": "Carryaway", "instances": 16, "metric_value": 0.9544, "depth": 11}
											if obj[16]>1.0:
												# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 12}
												if obj[11]<=2:
													# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 13}
													if obj[12]>7:
														# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 14}
														if obj[13]<=4:
															# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 15}
															if obj[15]<=1.0:
																# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[1]>0:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]>0:
																		return 'False'
																	elif obj[9]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[1]<=0:
																	# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[9]>0:
																		return 'True'
																	elif obj[9]<=0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[15]>1.0:
																return 'True'
															else: return 'True'
														elif obj[13]>4:
															return 'False'
														else: return 'False'
													elif obj[12]<=7:
														# {"feature": "Income", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[13]<=6:
															return 'False'
														elif obj[13]>6:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[11]>2:
													return 'False'
												else: return 'False'
											elif obj[16]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[18]>2.0:
											return 'True'
										else: return 'True'
									elif obj[7]>0:
										# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[12]>1:
											return 'False'
										elif obj[12]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]<=0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[11]<=3:
										return 'True'
									elif obj[11]>3:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[10]>0:
							# {"feature": "Income", "instances": 64, "metric_value": 0.8774, "depth": 7}
							if obj[13]<=6:
								# {"feature": "Passanger", "instances": 56, "metric_value": 0.9241, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Coffeehouse", "instances": 47, "metric_value": 0.8508, "depth": 9}
									if obj[15]>1.0:
										# {"feature": "Restaurantlessthan20", "instances": 27, "metric_value": 0.951, "depth": 10}
										if obj[17]<=3.0:
											# {"feature": "Gender", "instances": 24, "metric_value": 0.9799, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 12}
												if obj[18]<=1.0:
													# {"feature": "Temperature", "instances": 9, "metric_value": 0.9911, "depth": 13}
													if obj[3]<=55:
														# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 14}
														if obj[12]>6:
															return 'False'
														elif obj[12]<=6:
															# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[0]<=0:
																return 'True'
															elif obj[0]>0:
																return 'False'
															else: return 'False'
														else: return 'True'
													elif obj[3]>55:
														# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[0]<=0:
															return 'True'
														elif obj[0]>0:
															# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[8]>1:
																return 'True'
															elif obj[8]<=1:
																return 'False'
															else: return 'False'
														else: return 'True'
													else: return 'True'
												elif obj[18]>1.0:
													return 'False'
												else: return 'False'
											elif obj[7]>0:
												# {"feature": "Carryaway", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[16]>2.0:
													# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 13}
													if obj[8]<=3:
														# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 14}
														if obj[12]<=6:
															# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[0]<=0:
																# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[11]>0:
																	return 'True'
																elif obj[11]<=0:
																	return 'False'
																else: return 'False'
															elif obj[0]>0:
																return 'False'
															else: return 'False'
														elif obj[12]>6:
															return 'True'
														else: return 'True'
													elif obj[8]>3:
														return 'True'
													else: return 'True'
												elif obj[16]<=2.0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[17]>3.0:
											return 'False'
										else: return 'False'
									elif obj[15]<=1.0:
										# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.6098, "depth": 10}
										if obj[18]<=1.0:
											return 'False'
										elif obj[18]>1.0:
											# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[11]<=0:
												# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[3]>55:
													return 'True'
												elif obj[3]<=55:
													# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0]>0:
														return 'True'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[11]>0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>2:
									# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 9}
									if obj[11]>0:
										# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[12]<=9:
											# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[7]>0:
												return 'False'
											elif obj[7]<=0:
												# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[16]>1.0:
													return 'False'
												elif obj[16]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[12]>9:
											return 'True'
										else: return 'True'
									elif obj[11]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[13]>6:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>0:
					# {"feature": "Passanger", "instances": 215, "metric_value": 0.9886, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Coffeehouse", "instances": 145, "metric_value": 0.9356, "depth": 6}
						if obj[15]>1.0:
							# {"feature": "Age", "instances": 76, "metric_value": 0.9955, "depth": 7}
							if obj[8]<=6:
								# {"feature": "Income", "instances": 72, "metric_value": 0.986, "depth": 8}
								if obj[13]<=7:
									# {"feature": "Temperature", "instances": 68, "metric_value": 0.9944, "depth": 9}
									if obj[3]>30:
										# {"feature": "Education", "instances": 63, "metric_value": 0.9779, "depth": 10}
										if obj[11]<=3:
											# {"feature": "Restaurantlessthan20", "instances": 61, "metric_value": 0.967, "depth": 11}
											if obj[17]>1.0:
												# {"feature": "Occupation", "instances": 59, "metric_value": 0.9529, "depth": 12}
												if obj[12]>1:
													# {"feature": "Driving_to", "instances": 54, "metric_value": 0.9751, "depth": 13}
													if obj[0]>0:
														# {"feature": "Maritalstatus", "instances": 28, "metric_value": 0.8631, "depth": 14}
														if obj[9]<=2:
															# {"feature": "Time", "instances": 27, "metric_value": 0.8256, "depth": 15}
															if obj[4]<=0:
																# {"feature": "Carryaway", "instances": 16, "metric_value": 0.9544, "depth": 16}
																if obj[16]<=3.0:
																	# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 17}
																	if obj[18]>0.0:
																		# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 18}
																		if obj[19]<=0:
																			return 'False'
																		elif obj[19]>0:
																			# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 19}
																			if obj[7]<=0:
																				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[10]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=1:
																						return 'False'
																					else: return 'False'
																				elif obj[10]>0:
																					return 'False'
																				else: return 'False'
																			elif obj[7]>0:
																				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[20]>1:
																					return 'True'
																				elif obj[20]<=1:
																					return 'False'
																				else: return 'False'
																			else: return 'True'
																		else: return 'False'
																	elif obj[18]<=0.0:
																		return 'True'
																	else: return 'True'
																elif obj[16]>3.0:
																	# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[10]>0:
																		# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7]>0:
																			return 'True'
																		elif obj[7]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[10]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[4]>0:
																# {"feature": "Carryaway", "instances": 11, "metric_value": 0.4395, "depth": 16}
																if obj[16]>2.0:
																	return 'False'
																elif obj[16]<=2.0:
																	# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[7]>0:
																		return 'False'
																	elif obj[7]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'False'
														elif obj[9]>2:
															return 'True'
														else: return 'True'
													elif obj[0]<=0:
														# {"feature": "Gender", "instances": 26, "metric_value": 0.9957, "depth": 14}
														if obj[7]<=0:
															# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 15}
															if obj[18]>1.0:
																# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.994, "depth": 16}
																if obj[9]<=0:
																	# {"feature": "Children", "instances": 6, "metric_value": 0.9183, "depth": 17}
																	if obj[10]<=0:
																		# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 18}
																		if obj[4]<=0:
																			# {"feature": "Carryaway", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[16]>2.0:
																				# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[20]<=2:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			elif obj[16]<=2.0:
																				return 'False'
																			else: return 'False'
																		elif obj[4]>0:
																			return 'False'
																		else: return 'False'
																	elif obj[10]>0:
																		return 'True'
																	else: return 'True'
																elif obj[9]>0:
																	# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 17}
																	if obj[10]<=0:
																		return 'True'
																	elif obj[10]>0:
																		return 'False'
																	else: return 'False'
																else: return 'True'
															elif obj[18]<=1.0:
																return 'False'
															else: return 'False'
														elif obj[7]>0:
															# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.8454, "depth": 15}
															if obj[9]>0:
																# {"feature": "Carryaway", "instances": 6, "metric_value": 1.0, "depth": 16}
																if obj[16]<=3.0:
																	# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 17}
																	if obj[4]<=0:
																		# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 19}
																			if obj[18]<=2.0:
																				# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[19]<=0:
																					# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[20]<=2:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[4]>0:
																		return 'True'
																	else: return 'True'
																elif obj[16]>3.0:
																	return 'False'
																else: return 'False'
															elif obj[9]<=0:
																return 'True'
															else: return 'True'
														else: return 'True'
													else: return 'True'
												elif obj[12]<=1:
													return 'False'
												else: return 'False'
											elif obj[17]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[11]>3:
											return 'True'
										else: return 'True'
									elif obj[3]<=30:
										return 'True'
									else: return 'True'
								elif obj[13]>7:
									return 'False'
								else: return 'False'
							elif obj[8]>6:
								return 'True'
							else: return 'True'
						elif obj[15]<=1.0:
							# {"feature": "Maritalstatus", "instances": 69, "metric_value": 0.7813, "depth": 7}
							if obj[9]<=0:
								# {"feature": "Occupation", "instances": 43, "metric_value": 0.5186, "depth": 8}
								if obj[12]<=22:
									# {"feature": "Restaurant20to50", "instances": 42, "metric_value": 0.4537, "depth": 9}
									if obj[18]<=2.0:
										# {"feature": "Age", "instances": 38, "metric_value": 0.2975, "depth": 10}
										if obj[8]<=3:
											return 'False'
										elif obj[8]>3:
											# {"feature": "Children", "instances": 16, "metric_value": 0.5436, "depth": 11}
											if obj[10]>0:
												return 'False'
											elif obj[10]<=0:
												# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[13]>0:
													# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[4]<=0:
														# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11]>0:
															return 'True'
														elif obj[11]<=0:
															return 'False'
														else: return 'False'
													elif obj[4]>0:
														return 'True'
													else: return 'True'
												elif obj[13]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[18]>2.0:
										# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[0]>0:
											# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]>30:
												return 'False'
											elif obj[3]<=30:
												return 'True'
											else: return 'True'
										elif obj[0]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[12]>22:
									return 'True'
								else: return 'True'
							elif obj[9]>0:
								# {"feature": "Age", "instances": 26, "metric_value": 0.9829, "depth": 8}
								if obj[8]<=4:
									# {"feature": "Time", "instances": 21, "metric_value": 0.9984, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Income", "instances": 12, "metric_value": 0.8113, "depth": 10}
										if obj[13]<=4:
											# {"feature": "Driving_to", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[0]>0:
												# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[7]<=0:
													return 'True'
												elif obj[7]>0:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10]>0:
														return 'True'
													elif obj[10]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										elif obj[13]>4:
											return 'True'
										else: return 'True'
									elif obj[4]>0:
										# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[13]>0:
											# {"feature": "Driving_to", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[0]>0:
												return 'False'
											elif obj[0]<=0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7]<=0:
													return 'False'
												elif obj[7]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[13]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>4:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Age", "instances": 70, "metric_value": 0.962, "depth": 6}
						if obj[8]<=4:
							# {"feature": "Temperature", "instances": 58, "metric_value": 0.9124, "depth": 7}
							if obj[3]<=55:
								# {"feature": "Gender", "instances": 40, "metric_value": 0.8113, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Education", "instances": 24, "metric_value": 0.5436, "depth": 9}
									if obj[11]<=1:
										return 'True'
									elif obj[11]>1:
										# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 10}
										if obj[12]<=16:
											# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 11}
											if obj[15]<=3.0:
												# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[13]<=5:
													return 'True'
												elif obj[13]>5:
													# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9]<=0:
														return 'False'
													elif obj[9]>0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[15]>3.0:
												return 'False'
											else: return 'False'
										elif obj[12]>16:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[7]>0:
									# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 9}
									if obj[12]>2:
										# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[9]<=1:
											# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[11]<=0:
												return 'False'
											elif obj[11]>0:
												# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[10]>0:
													# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[13]>0:
														# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[18]<=1.0:
															return 'True'
														elif obj[18]>1.0:
															return 'False'
														else: return 'False'
													elif obj[13]<=0:
														return 'True'
													else: return 'True'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[9]>1:
											return 'True'
										else: return 'True'
									elif obj[12]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>55:
								# {"feature": "Carryaway", "instances": 18, "metric_value": 1.0, "depth": 8}
								if obj[16]>1.0:
									# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 9}
									if obj[12]>1:
										# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.8905, "depth": 10}
										if obj[15]<=3.0:
											# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 11}
											if obj[18]>0.0:
												# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 12}
												if obj[13]>0:
													return 'True'
												elif obj[13]<=0:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]>0:
														return 'True'
													elif obj[7]<=0:
														return 'False'
													else: return 'False'
												else: return 'True'
											elif obj[18]<=0.0:
												return 'False'
											else: return 'False'
										elif obj[15]>3.0:
											return 'False'
										else: return 'False'
									elif obj[12]<=1:
										return 'False'
									else: return 'False'
								elif obj[16]<=1.0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[8]>4:
							# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 7}
							if obj[12]<=9:
								return 'False'
							elif obj[12]>9:
								# {"feature": "Temperature", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]<=55:
									return 'True'
								elif obj[3]>55:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=0:
										# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=2:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=0:
												# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9]<=0:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10]<=1:
														# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11]<=3:
															# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13]<=7:
																# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[15]<=2.0:
																	# {"feature": "Carryaway", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[16]<=2.0:
																		# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17]<=1.0:
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
												else: return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[2]>1:
				# {"feature": "Driving_to", "instances": 99, "metric_value": 0.8725, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 75, "metric_value": 0.9311, "depth": 5}
					if obj[20]>1:
						# {"feature": "Maritalstatus", "instances": 47, "metric_value": 0.8196, "depth": 6}
						if obj[9]<=1:
							# {"feature": "Coffeehouse", "instances": 40, "metric_value": 0.8813, "depth": 7}
							if obj[15]<=3.0:
								# {"feature": "Income", "instances": 38, "metric_value": 0.8315, "depth": 8}
								if obj[13]<=4:
									# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.6098, "depth": 9}
									if obj[17]<=2.0:
										# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[8]>1:
											# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 11}
											if obj[7]>0:
												# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[12]>5:
													# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1]<=1:
														# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10]<=0:
															return 'False'
														elif obj[10]>0:
															return 'True'
														else: return 'True'
													elif obj[1]>1:
														return 'False'
													else: return 'False'
												elif obj[12]<=5:
													return 'False'
												else: return 'False'
											elif obj[7]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=1:
											return 'False'
										else: return 'False'
									elif obj[17]>2.0:
										return 'False'
									else: return 'False'
								elif obj[13]>4:
									# {"feature": "Education", "instances": 18, "metric_value": 0.9641, "depth": 9}
									if obj[11]<=2:
										# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[7]>0:
											# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[1]<=1:
												# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[8]<=4:
													return 'True'
												elif obj[8]>4:
													return 'False'
												else: return 'False'
											elif obj[1]>1:
												return 'False'
											else: return 'False'
										elif obj[7]<=0:
											return 'True'
										else: return 'True'
									elif obj[11]>2:
										# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[8]>2:
											return 'False'
										elif obj[8]<=2:
											# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12]<=9:
												return 'False'
											elif obj[12]>9:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[15]>3.0:
								return 'True'
							else: return 'True'
						elif obj[9]>1:
							return 'False'
						else: return 'False'
					elif obj[20]<=1:
						# {"feature": "Coffeehouse", "instances": 28, "metric_value": 1.0, "depth": 6}
						if obj[15]<=3.0:
							# {"feature": "Occupation", "instances": 25, "metric_value": 0.9896, "depth": 7}
							if obj[12]>5:
								# {"feature": "Carryaway", "instances": 21, "metric_value": 0.9984, "depth": 8}
								if obj[16]<=2.0:
									# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 9}
									if obj[11]<=1:
										# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[13]<=3:
											return 'True'
										elif obj[13]>3:
											# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[8]<=5:
												return 'False'
											elif obj[8]>5:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[11]>1:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[18]>-1.0:
											# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[10]>0:
												return 'False'
											elif obj[10]<=0:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7]>0:
													return 'False'
												elif obj[7]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[18]<=-1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[16]>2.0:
									# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[8]<=4:
										# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[18]>0.0:
											return 'False'
										elif obj[18]<=0.0:
											# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[17]>1.0:
												return 'True'
											elif obj[17]<=1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[8]>4:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[12]<=5:
								return 'True'
							else: return 'True'
						elif obj[15]>3.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.5436, "depth": 5}
					if obj[18]<=1.0:
						return 'False'
					elif obj[18]>1.0:
						# {"feature": "Coffeehouse", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[15]>1.0:
							# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[11]<=2:
								# {"feature": "Carryaway", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[16]>-1.0:
									return 'True'
								elif obj[16]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[11]>2:
								return 'False'
							else: return 'False'
						elif obj[15]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[14]<=0.0:
			# {"feature": "Carryaway", "instances": 588, "metric_value": 0.8193, "depth": 3}
			if obj[16]>-1.0:
				# {"feature": "Occupation", "instances": 580, "metric_value": 0.8085, "depth": 4}
				if obj[12]>1.460234613446337:
					# {"feature": "Time", "instances": 462, "metric_value": 0.8454, "depth": 5}
					if obj[4]<=3:
						# {"feature": "Coffeehouse", "instances": 390, "metric_value": 0.8749, "depth": 6}
						if obj[15]<=2.0:
							# {"feature": "Distance", "instances": 318, "metric_value": 0.9052, "depth": 7}
							if obj[20]<=2:
								# {"feature": "Education", "instances": 244, "metric_value": 0.9398, "depth": 8}
								if obj[11]<=2:
									# {"feature": "Restaurant20to50", "instances": 195, "metric_value": 0.9021, "depth": 9}
									if obj[18]<=2.0:
										# {"feature": "Restaurantlessthan20", "instances": 188, "metric_value": 0.8787, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Coupon_validity", "instances": 145, "metric_value": 0.916, "depth": 11}
											if obj[6]<=0:
												# {"feature": "Maritalstatus", "instances": 96, "metric_value": 0.9544, "depth": 12}
												if obj[9]<=3:
													# {"feature": "Temperature", "instances": 94, "metric_value": 0.9441, "depth": 13}
													if obj[3]>55:
														# {"feature": "Age", "instances": 48, "metric_value": 0.9887, "depth": 14}
														if obj[8]>0:
															# {"feature": "Income", "instances": 41, "metric_value": 0.9996, "depth": 15}
															if obj[13]>0:
																# {"feature": "Passanger", "instances": 35, "metric_value": 0.9947, "depth": 16}
																if obj[1]<=1:
																	# {"feature": "Gender", "instances": 27, "metric_value": 0.9751, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Children", "instances": 15, "metric_value": 0.9968, "depth": 18}
																		if obj[10]<=0:
																			# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 19}
																			if obj[19]<=0:
																				# {"feature": "Driving_to", "instances": 7, "metric_value": 0.9852, "depth": 20}
																				if obj[0]>0:
																					# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[0]<=0:
																					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[19]>0:
																				return 'True'
																			else: return 'True'
																		elif obj[10]>0:
																			# {"feature": "Driving_to", "instances": 5, "metric_value": 0.7219, "depth": 19}
																			if obj[0]<=1:
																				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[0]>1:
																				return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9183, "depth": 18}
																		if obj[19]<=0:
																			# {"feature": "Driving_to", "instances": 10, "metric_value": 0.971, "depth": 19}
																			if obj[0]<=1:
																				# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 21}
																					if obj[2]<=0:
																						return 'True'
																					else: return 'True'
																				elif obj[10]<=0:
																					return 'False'
																				else: return 'False'
																			elif obj[0]>1:
																				return 'True'
																			else: return 'True'
																		elif obj[19]>0:
																			return 'False'
																		else: return 'False'
																	else: return 'False'
																elif obj[1]>1:
																	# {"feature": "Gender", "instances": 8, "metric_value": 0.9544, "depth": 17}
																	if obj[7]<=0:
																		# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[0]<=0:
																			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 20}
																				if obj[10]>0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				elif obj[10]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[7]>0:
																		# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[0]<=0:
																			# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 19}
																			if obj[2]<=0:
																				# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 20}
																				if obj[10]<=1:
																					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 21}
																					if obj[19]<=0:
																						return 'True'
																					else: return 'True'
																				else: return 'True'
																			else: return 'True'
																		else: return 'True'
																	else: return 'True'
																else: return 'True'
															elif obj[13]<=0:
																# {"feature": "Driving_to", "instances": 6, "metric_value": 0.9183, "depth": 16}
																if obj[0]>1:
																	return 'True'
																elif obj[0]<=1:
																	# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[1]>0:
																		return 'False'
																	elif obj[1]<=0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'True'
														elif obj[8]<=0:
															# {"feature": "Driving_to", "instances": 7, "metric_value": 0.5917, "depth": 15}
															if obj[0]<=0:
																return 'False'
															elif obj[0]>0:
																# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[7]<=0:
																	# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[10]>0:
																		return 'False'
																	elif obj[10]<=0:
																		return 'True'
																	else: return 'True'
																elif obj[7]>0:
																	return 'False'
																else: return 'False'
															else: return 'False'
														else: return 'False'
													elif obj[3]<=55:
														# {"feature": "Children", "instances": 46, "metric_value": 0.859, "depth": 14}
														if obj[10]<=0:
															# {"feature": "Driving_to", "instances": 24, "metric_value": 0.9799, "depth": 15}
															if obj[0]>0:
																# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9341, "depth": 16}
																if obj[19]>0:
																	# {"feature": "Gender", "instances": 12, "metric_value": 1.0, "depth": 17}
																	if obj[7]>0:
																		# {"feature": "Age", "instances": 8, "metric_value": 0.9544, "depth": 18}
																		if obj[8]>0:
																			# {"feature": "Income", "instances": 6, "metric_value": 1.0, "depth": 19}
																			if obj[13]>0:
																				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 20}
																				if obj[1]<=1:
																					# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 21}
																					if obj[2]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			elif obj[13]<=0:
																				return 'True'
																			else: return 'True'
																		elif obj[8]<=0:
																			return 'False'
																		else: return 'False'
																	elif obj[7]<=0:
																		# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[13]>3:
																			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[1]<=1:
																				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[2]<=0:
																					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[8]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		elif obj[13]<=3:
																			return 'True'
																		else: return 'True'
																	else: return 'True'
																elif obj[19]<=0:
																	# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 17}
																	if obj[8]<=3:
																		# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[7]>0:
																			return 'False'
																		elif obj[7]<=0:
																			# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[13]<=0:
																				return 'False'
																			elif obj[13]>0:
																				return 'True'
																			else: return 'True'
																		else: return 'False'
																	elif obj[8]>3:
																		return 'False'
																	else: return 'False'
																else: return 'False'
															elif obj[0]<=0:
																# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 16}
																if obj[7]<=0:
																	return 'True'
																elif obj[7]>0:
																	# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[8]<=1:
																		return 'False'
																	elif obj[8]>1:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'True'
														elif obj[10]>0:
															# {"feature": "Direction_same", "instances": 22, "metric_value": 0.5746, "depth": 15}
															if obj[19]<=0:
																# {"feature": "Weather", "instances": 13, "metric_value": 0.7793, "depth": 16}
																if obj[2]>0:
																	return 'False'
																elif obj[2]<=0:
																	# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 17}
																	if obj[8]<=6:
																		# {"feature": "Driving_to", "instances": 4, "metric_value": 0.8113, "depth": 18}
																		if obj[0]>0:
																			return 'False'
																		elif obj[0]<=0:
																			return 'True'
																		else: return 'True'
																	elif obj[8]>6:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															elif obj[19]>0:
																return 'False'
															else: return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[9]>3:
													return 'True'
												else: return 'True'
											elif obj[6]>0:
												# {"feature": "Passanger", "instances": 49, "metric_value": 0.8031, "depth": 12}
												if obj[1]>1:
													# {"feature": "Driving_to", "instances": 29, "metric_value": 0.9784, "depth": 13}
													if obj[0]<=0:
														# {"feature": "Age", "instances": 20, "metric_value": 0.7219, "depth": 14}
														if obj[8]<=3:
															# {"feature": "Income", "instances": 15, "metric_value": 0.3534, "depth": 15}
															if obj[13]<=5:
																return 'False'
															elif obj[13]>5:
																# {"feature": "Children", "instances": 5, "metric_value": 0.7219, "depth": 16}
																if obj[10]>0:
																	return 'False'
																elif obj[10]<=0:
																	# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[2]<=0:
																		return 'False'
																	elif obj[2]>0:
																		return 'True'
																	else: return 'True'
																else: return 'False'
															else: return 'False'
														elif obj[8]>3:
															# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[2]<=0:
																# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[3]>30:
																	# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[7]<=0:
																		return 'True'
																	elif obj[7]>0:
																		return 'False'
																	else: return 'False'
																elif obj[3]<=30:
																	return 'False'
																else: return 'False'
															elif obj[2]>0:
																return 'True'
															else: return 'True'
														else: return 'True'
													elif obj[0]>0:
														# {"feature": "Gender", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[7]<=0:
															return 'True'
														elif obj[7]>0:
															# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3]>30:
																return 'False'
															elif obj[3]<=30:
																return 'True'
															else: return 'True'
														else: return 'False'
													else: return 'True'
												elif obj[1]<=1:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[17]<=1.0:
											# {"feature": "Income", "instances": 43, "metric_value": 0.6931, "depth": 11}
											if obj[13]>2:
												# {"feature": "Age", "instances": 33, "metric_value": 0.4395, "depth": 12}
												if obj[8]<=6:
													# {"feature": "Weather", "instances": 31, "metric_value": 0.2056, "depth": 13}
													if obj[2]<=0:
														return 'False'
													elif obj[2]>0:
														# {"feature": "Driving_to", "instances": 9, "metric_value": 0.5033, "depth": 14}
														if obj[0]<=0:
															return 'False'
														elif obj[0]>0:
															# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[1]>1:
																return 'False'
															elif obj[1]<=1:
																return 'True'
															else: return 'True'
														else: return 'False'
													else: return 'False'
												elif obj[8]>6:
													return 'True'
												else: return 'True'
											elif obj[13]<=2:
												# {"feature": "Temperature", "instances": 10, "metric_value": 1.0, "depth": 12}
												if obj[3]>55:
													# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1]<=2:
														return 'False'
													elif obj[1]>2:
														return 'True'
													else: return 'True'
												elif obj[3]<=55:
													# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[1]<=2:
														return 'True'
													elif obj[1]>2:
														return 'False'
													else: return 'False'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[18]>2.0:
										# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[6]>0:
											return 'True'
										elif obj[6]<=0:
											# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0]>0:
												return 'False'
											elif obj[0]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'True'
								elif obj[11]>2:
									# {"feature": "Income", "instances": 49, "metric_value": 0.9997, "depth": 9}
									if obj[13]<=3:
										# {"feature": "Driving_to", "instances": 27, "metric_value": 0.951, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Temperature", "instances": 15, "metric_value": 0.8366, "depth": 11}
											if obj[3]>55:
												# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[8]<=2:
													# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 13}
													if obj[6]>0:
														# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 14}
														if obj[1]<=1:
															return 'False'
														elif obj[1]>1:
															return 'True'
														else: return 'True'
													elif obj[6]<=0:
														return 'True'
													else: return 'True'
												elif obj[8]>2:
													return 'False'
												else: return 'False'
											elif obj[3]<=55:
												return 'False'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Gender", "instances": 12, "metric_value": 1.0, "depth": 11}
											if obj[7]>0:
												# {"feature": "Weather", "instances": 10, "metric_value": 0.971, "depth": 12}
												if obj[2]<=0:
													# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9183, "depth": 13}
													if obj[9]>2:
														# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[6]<=0:
															# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 15}
															if obj[19]>0:
																# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[10]>0:
																	return 'True'
																elif obj[10]<=0:
																	return 'False'
																else: return 'False'
															elif obj[19]<=0:
																return 'False'
															else: return 'False'
														elif obj[6]>0:
															return 'True'
														else: return 'True'
													elif obj[9]<=2:
														return 'False'
													else: return 'False'
												elif obj[2]>0:
													return 'True'
												else: return 'True'
											elif obj[7]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[13]>3:
										# {"feature": "Temperature", "instances": 22, "metric_value": 0.9024, "depth": 10}
										if obj[3]>30:
											# {"feature": "Maritalstatus", "instances": 14, "metric_value": 0.3712, "depth": 11}
											if obj[9]<=2:
												return 'True'
											elif obj[9]>2:
												return 'False'
											else: return 'False'
										elif obj[3]<=30:
											# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.8113, "depth": 11}
											if obj[9]>0:
												# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[1]<=1:
													# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[2]>0:
														return 'True'
													elif obj[2]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]>1:
													return 'False'
												else: return 'False'
											elif obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'True'
							elif obj[20]>2:
								# {"feature": "Passanger", "instances": 74, "metric_value": 0.7273, "depth": 8}
								if obj[1]<=1:
									# {"feature": "Children", "instances": 73, "metric_value": 0.7052, "depth": 9}
									if obj[10]<=0:
										# {"feature": "Education", "instances": 41, "metric_value": 0.839, "depth": 10}
										if obj[11]>0:
											# {"feature": "Income", "instances": 25, "metric_value": 0.971, "depth": 11}
											if obj[13]<=5:
												# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.7642, "depth": 12}
												if obj[18]>0.0:
													# {"feature": "Restaurantlessthan20", "instances": 17, "metric_value": 0.6723, "depth": 13}
													if obj[17]<=2.0:
														# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.8113, "depth": 14}
														if obj[9]>0:
															# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 15}
															if obj[7]>0:
																# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 16}
																if obj[2]<=0:
																	# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 17}
																	if obj[8]<=0:
																		# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[0]<=1:
																			# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[3]<=55:
																				# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[6]<=0:
																					# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 21}
																					if obj[19]<=0:
																						return 'False'
																					else: return 'False'
																				else: return 'False'
																			else: return 'False'
																		else: return 'False'
																	elif obj[8]>0:
																		return 'False'
																	else: return 'False'
																elif obj[2]>0:
																	return 'False'
																else: return 'False'
															elif obj[7]<=0:
																# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[0]<=1:
																	return 'True'
																elif obj[0]>1:
																	return 'False'
																else: return 'False'
															else: return 'True'
														elif obj[9]<=0:
															return 'False'
														else: return 'False'
													elif obj[17]>2.0:
														return 'False'
													else: return 'False'
												elif obj[18]<=0.0:
													return 'True'
												else: return 'True'
											elif obj[13]>5:
												# {"feature": "Gender", "instances": 7, "metric_value": 0.5917, "depth": 12}
												if obj[7]<=0:
													return 'True'
												elif obj[7]>0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[11]<=0:
											# {"feature": "Income", "instances": 16, "metric_value": 0.3373, "depth": 11}
											if obj[13]>2:
												return 'False'
											elif obj[13]<=2:
												# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[18]>1.0:
													return 'False'
												elif obj[18]<=1.0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'False'
									elif obj[10]>0:
										# {"feature": "Age", "instances": 32, "metric_value": 0.4489, "depth": 10}
										if obj[8]<=2:
											return 'False'
										elif obj[8]>2:
											# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 11}
											if obj[11]<=1:
												# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[2]<=1:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[7]<=0:
														return 'False'
													elif obj[7]>0:
														return 'True'
													else: return 'True'
												elif obj[2]>1:
													return 'True'
												else: return 'True'
											elif obj[11]>1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[1]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[15]>2.0:
							# {"feature": "Education", "instances": 72, "metric_value": 0.6813, "depth": 7}
							if obj[11]>1:
								# {"feature": "Age", "instances": 42, "metric_value": 0.3712, "depth": 8}
								if obj[8]<=3:
									return 'False'
								elif obj[8]>3:
									# {"feature": "Driving_to", "instances": 18, "metric_value": 0.65, "depth": 9}
									if obj[0]>1:
										# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[18]<=1.0:
											# {"feature": "Temperature", "instances": 7, "metric_value": 0.5917, "depth": 11}
											if obj[3]<=55:
												return 'False'
											elif obj[3]>55:
												# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[19]>0:
													return 'True'
												elif obj[19]<=0:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[18]>1.0:
											# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=55:
												return 'True'
											elif obj[3]>55:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[11]<=1:
								# {"feature": "Age", "instances": 30, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=5:
									# {"feature": "Temperature", "instances": 25, "metric_value": 0.971, "depth": 9}
									if obj[3]<=55:
										# {"feature": "Income", "instances": 14, "metric_value": 0.7496, "depth": 10}
										if obj[13]<=6:
											return 'False'
										elif obj[13]>6:
											# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[17]<=3.0:
												# {"feature": "Weather", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[2]>1:
													# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[0]>0:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7]>0:
															return 'True'
														elif obj[7]<=0:
															return 'False'
														else: return 'False'
													elif obj[0]<=0:
														return 'False'
													else: return 'False'
												elif obj[2]<=1:
													return 'False'
												else: return 'False'
											elif obj[17]>3.0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[3]>55:
										# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 10}
										if obj[13]<=6:
											# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[18]<=1.0:
												return 'True'
											elif obj[18]>1.0:
												# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[0]>1:
													return 'True'
												elif obj[0]<=1:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[13]>6:
											# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[1]>1:
												# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[0]<=0:
													# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[20]>1:
														return 'False'
													elif obj[20]<=1:
														return 'True'
													else: return 'True'
												elif obj[0]>0:
													return 'True'
												else: return 'True'
											elif obj[1]<=1:
												return 'False'
											else: return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]>5:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>3:
						# {"feature": "Distance", "instances": 72, "metric_value": 0.6167, "depth": 6}
						if obj[20]<=1:
							# {"feature": "Gender", "instances": 44, "metric_value": 0.7732, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.9544, "depth": 8}
								if obj[6]<=0:
									# {"feature": "Passanger", "instances": 19, "metric_value": 0.998, "depth": 9}
									if obj[1]>0:
										# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.8631, "depth": 10}
										if obj[15]<=1.0:
											# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 11}
											if obj[8]>0:
												# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 12}
												if obj[9]<=1:
													# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[17]<=2.0:
														return 'True'
													elif obj[17]>2.0:
														# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10]>0:
															return 'True'
														elif obj[10]<=0:
															return 'False'
														else: return 'False'
													else: return 'True'
												elif obj[9]>1:
													return 'False'
												else: return 'False'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										elif obj[15]>1.0:
											return 'False'
										else: return 'False'
									elif obj[1]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]>0:
								# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.2864, "depth": 8}
								if obj[17]>1.0:
									return 'False'
								elif obj[17]<=1.0:
									# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]>3:
										return 'False'
									elif obj[8]<=3:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[20]>1:
							# {"feature": "Education", "instances": 28, "metric_value": 0.2223, "depth": 7}
							if obj[11]<=3:
								return 'False'
							elif obj[11]>3:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]<=0:
									return 'True'
								elif obj[8]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[12]<=1.460234613446337:
					# {"feature": "Age", "instances": 118, "metric_value": 0.6162, "depth": 5}
					if obj[8]<=4:
						# {"feature": "Restaurantlessthan20", "instances": 82, "metric_value": 0.4208, "depth": 6}
						if obj[17]<=2.0:
							# {"feature": "Time", "instances": 61, "metric_value": 0.2082, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 8}
								if obj[18]<=1.0:
									return 'False'
								elif obj[18]>1.0:
									# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[0]>0:
										# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]>55:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6]<=0:
												return 'True'
											elif obj[6]>0:
												return 'False'
											else: return 'False'
										elif obj[3]<=55:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[17]>2.0:
							# {"feature": "Driving_to", "instances": 21, "metric_value": 0.7919, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Weather", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[2]>0:
									# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 9}
									if obj[15]>0.0:
										return 'False'
									elif obj[15]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[2]<=0:
									# {"feature": "Income", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[13]<=4:
										# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[3]>30:
											return 'False'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									elif obj[13]>4:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[8]>4:
						# {"feature": "Income", "instances": 36, "metric_value": 0.888, "depth": 6}
						if obj[13]<=6:
							# {"feature": "Direction_same", "instances": 27, "metric_value": 0.9751, "depth": 7}
							if obj[19]<=0:
								# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.995, "depth": 8}
								if obj[17]<=2.0:
									# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.976, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Temperature", "instances": 14, "metric_value": 0.9852, "depth": 10}
										if obj[3]<=55:
											# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 11}
											if obj[15]>0.0:
												# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[4]>0:
													return 'False'
												elif obj[4]<=0:
													# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2]>0:
														return 'False'
													elif obj[2]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[15]<=0.0:
												# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[20]>1:
													return 'True'
												elif obj[20]<=1:
													# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2]>0:
														return 'False'
													elif obj[2]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											else: return 'True'
										elif obj[3]>55:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 10}
										if obj[1]<=2:
											return 'False'
										elif obj[1]>2:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7]<=0:
												return 'False'
											elif obj[7]>0:
												return 'True'
											else: return 'True'
										else: return 'False'
									else: return 'False'
								elif obj[17]>2.0:
									return 'True'
								else: return 'True'
							elif obj[19]>0:
								return 'False'
							else: return 'False'
						elif obj[13]>6:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[16]<=-1.0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>55:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=55:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
