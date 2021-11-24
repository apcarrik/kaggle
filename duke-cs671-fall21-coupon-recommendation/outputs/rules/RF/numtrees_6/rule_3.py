def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Bar", "instances": 170, "metric_value": 0.9674, "depth": 1}
	if obj[14]<=2.0:
		# {"feature": "Coffeehouse", "instances": 154, "metric_value": 0.9852, "depth": 2}
		if obj[15]<=1.0:
			# {"feature": "Passanger", "instances": 85, "metric_value": 0.9975, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Income", "instances": 57, "metric_value": 0.9495, "depth": 4}
				if obj[13]<=3:
					# {"feature": "Children", "instances": 29, "metric_value": 0.7973, "depth": 5}
					if obj[10]<=0:
						# {"feature": "Driving_to", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[0]>0:
							# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[17]<=3.0:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[5]>0:
									# {"feature": "Gender", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[20]>1:
											# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[2]<=1:
												return 'False'
											elif obj[2]>1:
												return 'True'
											else: return 'True'
										elif obj[20]<=1:
											return 'True'
										else: return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							elif obj[17]>3.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[10]>0:
						# {"feature": "Restaurantlessthan20", "instances": 14, "metric_value": 0.3712, "depth": 6}
						if obj[17]<=3.0:
							return 'False'
						elif obj[17]>3.0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[13]>3:
					# {"feature": "Driving_to", "instances": 28, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Maritalstatus", "instances": 19, "metric_value": 0.9495, "depth": 6}
						if obj[9]<=1:
							# {"feature": "Weather", "instances": 15, "metric_value": 0.9968, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[5]<=2:
									# {"feature": "Temperature", "instances": 7, "metric_value": 0.5917, "depth": 9}
									if obj[3]>30:
										return 'True'
									elif obj[3]<=30:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=1:
											return 'False'
										elif obj[8]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>2:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[12]>0:
										return 'False'
									elif obj[12]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[9]>1:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Temperature", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[3]<=55:
							return 'True'
						elif obj[3]>55:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Coupon_validity", "instances": 28, "metric_value": 0.9059, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Coupon", "instances": 14, "metric_value": 0.5917, "depth": 5}
					if obj[5]>1:
						# {"feature": "Gender", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[7]>0:
							return 'True'
						elif obj[7]<=0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[8]>0:
								return 'True'
							elif obj[8]<=0:
								# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>55:
									return 'False'
								elif obj[3]<=55:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]>0:
					# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[18]>0.0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[11]>0:
							# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[9]<=1:
								# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[9]>1:
								return 'True'
							else: return 'True'
						elif obj[11]<=0:
							return 'True'
						else: return 'True'
					elif obj[18]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]>1.0:
			# {"feature": "Carryaway", "instances": 69, "metric_value": 0.8865, "depth": 3}
			if obj[16]>1.0:
				# {"feature": "Education", "instances": 61, "metric_value": 0.8047, "depth": 4}
				if obj[11]>0:
					# {"feature": "Temperature", "instances": 43, "metric_value": 0.9103, "depth": 5}
					if obj[3]<=55:
						# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 6}
						if obj[18]>0.0:
							# {"feature": "Driving_to", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 8}
								if obj[8]<=4:
									# {"feature": "Income", "instances": 16, "metric_value": 0.9887, "depth": 9}
									if obj[13]>1:
										# {"feature": "Children", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[10]>0:
											# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 11}
											if obj[19]<=0:
												# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 12}
												if obj[5]>0:
													# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 13}
													if obj[4]<=2:
														return 'True'
													elif obj[4]>2:
														# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[6]>0:
															return 'False'
														elif obj[6]<=0:
															return 'True'
														else: return 'True'
													else: return 'False'
												elif obj[5]<=0:
													# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7]>0:
														return 'False'
													elif obj[7]<=0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[19]>0:
												return 'False'
											else: return 'False'
										elif obj[10]<=0:
											return 'False'
										else: return 'False'
									elif obj[13]<=1:
										return 'False'
									else: return 'False'
								elif obj[8]>4:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[18]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[3]>55:
						# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 6}
						if obj[12]>4:
							return 'True'
						elif obj[12]<=4:
							# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[1]>0:
									return 'True'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							elif obj[8]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[11]<=0:
					# {"feature": "Children", "instances": 18, "metric_value": 0.3095, "depth": 5}
					if obj[10]<=0:
						return 'True'
					elif obj[10]>0:
						# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]<=0:
							return 'True'
						elif obj[0]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[16]<=1.0:
				# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[12]<=14:
					return 'False'
				elif obj[12]>14:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[14]>2.0:
		# {"feature": "Weather", "instances": 16, "metric_value": 0.3373, "depth": 2}
		if obj[2]<=1:
			return 'True'
		elif obj[2]>1:
			# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=0:
				return 'True'
			elif obj[0]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
