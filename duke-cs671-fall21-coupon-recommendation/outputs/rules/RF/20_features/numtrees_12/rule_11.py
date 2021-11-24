def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9465, "depth": 1}
	if obj[5]>0:
		# {"feature": "Occupation", "instances": 69, "metric_value": 0.8281, "depth": 2}
		if obj[12]<=6:
			# {"feature": "Age", "instances": 40, "metric_value": 0.6098, "depth": 3}
			if obj[8]<=2:
				# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.2668, "depth": 4}
				if obj[9]<=1:
					return 'True'
				elif obj[9]>1:
					return 'False'
				else: return 'False'
			elif obj[8]>2:
				# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.8524, "depth": 4}
				if obj[17]<=1.0:
					# {"feature": "Income", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[13]>2:
						# {"feature": "Gender", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[14]>1.0:
								return 'True'
							else: return 'True'
						elif obj[7]>0:
							return 'True'
						else: return 'True'
					elif obj[13]<=2:
						return 'False'
					else: return 'False'
				elif obj[17]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[12]>6:
			# {"feature": "Distance", "instances": 29, "metric_value": 0.9784, "depth": 3}
			if obj[19]<=2:
				# {"feature": "Weather", "instances": 26, "metric_value": 0.9306, "depth": 4}
				if obj[2]<=0:
					# {"feature": "Direction_same", "instances": 22, "metric_value": 0.976, "depth": 5}
					if obj[18]<=0:
						# {"feature": "Driving_to", "instances": 18, "metric_value": 1.0, "depth": 6}
						if obj[0]<=0:
							# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[4]>2:
								# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[14]<=1.0:
									# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[13]>2:
										# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]>1:
											# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=80:
												# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]<=1:
														# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8]<=4:
															# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9]<=0:
																# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10]<=0:
																	# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[11]<=0:
																		# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[15]<=4.0:
																			# {"feature": "Restaurantlessthan20", "instances": 2, "metric_value": 1.0, "depth": 19}
																			if obj[16]<=2.0:
																				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 20}
																				if obj[17]<=2.0:
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
										elif obj[1]<=1:
											return 'True'
										else: return 'True'
									elif obj[13]<=2:
										return 'False'
									else: return 'False'
								elif obj[14]>1.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=2:
								return 'True'
							else: return 'True'
						elif obj[0]>0:
							# {"feature": "Restaurantlessthan20", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[16]>1.0:
								return 'False'
							elif obj[16]<=1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[18]>0:
						return 'True'
					else: return 'True'
				elif obj[2]>0:
					return 'True'
				else: return 'True'
			elif obj[19]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=0:
		# {"feature": "Education", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[11]<=3:
			return 'False'
		elif obj[11]>3:
			# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[8]>1:
				return 'True'
			elif obj[8]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
