def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 204, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Bar", "instances": 147, "metric_value": 0.979, "depth": 2}
		if obj[14]<=1.0:
			# {"feature": "Coffeehouse", "instances": 87, "metric_value": 0.9991, "depth": 3}
			if obj[15]<=3.0:
				# {"feature": "Occupation", "instances": 81, "metric_value": 0.9911, "depth": 4}
				if obj[12]<=21:
					# {"feature": "Restaurant20to50", "instances": 78, "metric_value": 0.9829, "depth": 5}
					if obj[18]<=1.0:
						# {"feature": "Coupon_validity", "instances": 49, "metric_value": 0.9113, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Coupon", "instances": 32, "metric_value": 0.9887, "depth": 7}
							if obj[5]>0:
								# {"feature": "Time", "instances": 24, "metric_value": 0.995, "depth": 8}
								if obj[4]>0:
									# {"feature": "Age", "instances": 18, "metric_value": 0.9641, "depth": 9}
									if obj[8]<=4:
										# {"feature": "Education", "instances": 14, "metric_value": 1.0, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Driving_to", "instances": 12, "metric_value": 0.9799, "depth": 11}
											if obj[0]>0:
												# {"feature": "Income", "instances": 8, "metric_value": 0.9544, "depth": 12}
												if obj[13]<=5:
													# {"feature": "Weather", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[2]<=0:
														# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[3]<=55:
															return 'True'
														elif obj[3]>55:
															return 'False'
														else: return 'False'
													elif obj[2]>0:
														return 'False'
													else: return 'False'
												elif obj[13]>5:
													return 'True'
												else: return 'True'
											elif obj[0]<=0:
												return 'False'
											else: return 'False'
										elif obj[11]>2:
											return 'True'
										else: return 'True'
									elif obj[8]>4:
										return 'False'
									else: return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0:
								# {"feature": "Temperature", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[3]<=55:
									return 'False'
								elif obj[3]>55:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[6]>0:
							# {"feature": "Direction_same", "instances": 17, "metric_value": 0.5226, "depth": 7}
							if obj[19]<=0:
								return 'False'
							elif obj[19]>0:
								# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9]>0:
									return 'False'
								elif obj[9]<=0:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>2:
										return 'True'
									elif obj[5]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[18]>1.0:
						# {"feature": "Temperature", "instances": 29, "metric_value": 0.9784, "depth": 6}
						if obj[3]>30:
							# {"feature": "Coupon_validity", "instances": 24, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								# {"feature": "Time", "instances": 14, "metric_value": 1.0, "depth": 8}
								if obj[4]>0:
									# {"feature": "Driving_to", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[0]>0:
										# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 10}
										if obj[5]<=3:
											return 'False'
										elif obj[5]>3:
											# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]>1:
												return 'False'
											elif obj[8]<=1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[0]<=0:
										# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[8]<=4:
											return 'True'
										elif obj[8]>4:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]<=0:
								# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[5]>0:
									return 'True'
								elif obj[5]<=0:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=30:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[12]>21:
					return 'True'
				else: return 'True'
			elif obj[15]>3.0:
				return 'True'
			else: return 'True'
		elif obj[14]>1.0:
			# {"feature": "Education", "instances": 60, "metric_value": 0.8366, "depth": 3}
			if obj[11]>0:
				# {"feature": "Coupon", "instances": 42, "metric_value": 0.9403, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Distance", "instances": 31, "metric_value": 0.8238, "depth": 5}
					if obj[20]<=2:
						# {"feature": "Age", "instances": 24, "metric_value": 0.9183, "depth": 6}
						if obj[8]>0:
							# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.8454, "depth": 7}
							if obj[9]>0:
								# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 8}
								if obj[12]<=10:
									# {"feature": "Carryaway", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[16]>2.0:
										# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[7]<=0:
											return 'True'
										elif obj[7]>0:
											# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6]>0:
												return 'True'
											elif obj[6]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[16]<=2.0:
										# {"feature": "Driving_to", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[0]>0:
											# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[13]<=4:
												return 'True'
											elif obj[13]>4:
												return 'False'
											else: return 'False'
										elif obj[0]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[12]>10:
									return 'False'
								else: return 'False'
							elif obj[9]<=0:
								# {"feature": "Driving_to", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[0]>0:
									# {"feature": "Carryaway", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[16]<=2.0:
										return 'True'
									elif obj[16]>2.0:
										return 'False'
									else: return 'False'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]<=0:
							return 'False'
						else: return 'False'
					elif obj[20]>2:
						return 'True'
					else: return 'True'
				elif obj[5]>3:
					# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[15]>2.0:
						# {"feature": "Weather", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[15]<=2.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[11]<=0:
				# {"feature": "Age", "instances": 18, "metric_value": 0.3095, "depth": 4}
				if obj[8]<=6:
					return 'True'
				elif obj[8]>6:
					# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Age", "instances": 57, "metric_value": 0.7077, "depth": 2}
		if obj[8]>1:
			# {"feature": "Maritalstatus", "instances": 38, "metric_value": 0.3985, "depth": 3}
			if obj[9]<=2:
				# {"feature": "Time", "instances": 35, "metric_value": 0.1872, "depth": 4}
				if obj[4]<=3:
					return 'True'
				elif obj[4]>3:
					# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[11]<=2:
						return 'True'
					elif obj[11]>2:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[12]<=4:
							return 'False'
						elif obj[12]>4:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]>2:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[10]<=0:
					return 'False'
				elif obj[10]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[8]<=1:
			# {"feature": "Restaurantlessthan20", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[17]>1.0:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[5]>2:
					# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[13]>1:
						return 'True'
					elif obj[13]<=1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=3:
							return 'False'
						elif obj[4]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=2:
					# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[12]>1:
						return 'False'
					elif obj[12]<=1:
						# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=30:
							return 'False'
						elif obj[3]>30:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'False'
			elif obj[17]<=1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
