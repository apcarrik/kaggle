def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Age", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[8]>1:
		# {"feature": "Education", "instances": 88, "metric_value": 0.9865, "depth": 2}
		if obj[11]<=3:
			# {"feature": "Coupon", "instances": 84, "metric_value": 0.9737, "depth": 3}
			if obj[5]>0:
				# {"feature": "Direction_same", "instances": 73, "metric_value": 0.9934, "depth": 4}
				if obj[18]<=0:
					# {"feature": "Occupation", "instances": 63, "metric_value": 0.9691, "depth": 5}
					if obj[12]>1:
						# {"feature": "Bar", "instances": 57, "metric_value": 0.9348, "depth": 6}
						if obj[14]<=2.0:
							# {"feature": "Restaurantlessthan20", "instances": 52, "metric_value": 0.8905, "depth": 7}
							if obj[16]>1.0:
								# {"feature": "Income", "instances": 46, "metric_value": 0.8281, "depth": 8}
								if obj[13]<=6:
									# {"feature": "Restaurant20to50", "instances": 43, "metric_value": 0.8542, "depth": 9}
									if obj[17]<=1.0:
										# {"feature": "Driving_to", "instances": 28, "metric_value": 0.7496, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.5917, "depth": 11}
											if obj[9]>0:
												return 'False'
											elif obj[9]<=0:
												# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[1]>0:
													# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 13}
													if obj[6]>0:
														# {"feature": "Temperature", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[3]>55:
															# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[15]>1.0:
																return 'False'
															elif obj[15]<=1.0:
																return 'True'
															else: return 'True'
														elif obj[3]<=55:
															return 'True'
														else: return 'True'
													elif obj[6]<=0:
														return 'False'
													else: return 'False'
												elif obj[1]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[0]>1:
											# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[6]>0:
												return 'False'
											elif obj[6]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[17]>1.0:
										# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 10}
										if obj[4]<=1:
											# {"feature": "Maritalstatus", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[9]<=1:
												return 'False'
											elif obj[9]>1:
												# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[2]<=0:
													return 'False'
												elif obj[2]>0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[4]>1:
											# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[15]>0.0:
												return 'True'
											elif obj[15]<=0.0:
												# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]>0:
													return 'False'
												elif obj[6]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[13]>6:
									return 'False'
								else: return 'False'
							elif obj[16]<=1.0:
								# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=0:
									return 'True'
								elif obj[9]>0:
									# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>30:
										return 'False'
									elif obj[3]<=30:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[14]>2.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]<=2:
								return 'True'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]<=1:
						# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[10]>0:
							return 'True'
						elif obj[10]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[18]>0:
					# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[12]>5:
						return 'True'
					elif obj[12]<=5:
						# {"feature": "Driving_to", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[9]<=1:
								return 'False'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]<=0:
				# {"feature": "Passanger", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]>3:
			return 'True'
		else: return 'True'
	elif obj[8]<=1:
		# {"feature": "Restaurant20to50", "instances": 39, "metric_value": 0.8213, "depth": 2}
		if obj[17]<=1.0:
			# {"feature": "Occupation", "instances": 25, "metric_value": 0.5294, "depth": 3}
			if obj[12]<=20:
				# {"feature": "Income", "instances": 22, "metric_value": 0.2668, "depth": 4}
				if obj[13]<=6:
					return 'True'
				elif obj[13]>6:
					return 'False'
				else: return 'False'
			elif obj[12]>20:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[17]>1.0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[13]>2:
					# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]>2:
						return 'False'
					elif obj[5]<=2:
						# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=1:
							return 'True'
						elif obj[2]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[13]<=2:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
