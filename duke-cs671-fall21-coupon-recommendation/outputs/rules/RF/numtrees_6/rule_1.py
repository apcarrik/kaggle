def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Carryaway", "instances": 170, "metric_value": 0.9856, "depth": 1}
	if obj[16]>0.0:
		# {"feature": "Driving_to", "instances": 165, "metric_value": 0.9776, "depth": 2}
		if obj[0]<=0:
			# {"feature": "Distance", "instances": 90, "metric_value": 0.8813, "depth": 3}
			if obj[20]>1:
				# {"feature": "Passanger", "instances": 51, "metric_value": 0.9774, "depth": 4}
				if obj[1]<=2:
					# {"feature": "Income", "instances": 32, "metric_value": 0.9972, "depth": 5}
					if obj[13]<=6:
						# {"feature": "Restaurant20to50", "instances": 28, "metric_value": 0.9963, "depth": 6}
						if obj[18]<=2.0:
							# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 7}
							if obj[5]<=3:
								# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.9544, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9957, "depth": 9}
									if obj[15]>1.0:
										# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[10]>0:
											# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 11}
											if obj[14]<=1.0:
												return 'True'
											elif obj[14]>1.0:
												return 'False'
											else: return 'False'
										elif obj[10]<=0:
											return 'False'
										else: return 'False'
									elif obj[15]<=1.0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[4]<=0:
											# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]<=3:
												return 'True'
											elif obj[8]>3:
												return 'False'
											else: return 'False'
										elif obj[4]>0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>3:
								# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[17]>0.0:
									return 'False'
								elif obj[17]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[18]>2.0:
							return 'True'
						else: return 'True'
					elif obj[13]>6:
						return 'False'
					else: return 'False'
				elif obj[1]>2:
					# {"feature": "Coupon", "instances": 19, "metric_value": 0.7425, "depth": 5}
					if obj[5]>0:
						# {"feature": "Income", "instances": 16, "metric_value": 0.5436, "depth": 6}
						if obj[13]>2:
							return 'True'
						elif obj[13]<=2:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[18]>0.0:
								# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[11]>0:
									return 'True'
								elif obj[11]<=0:
									# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]>0:
										return 'False'
									elif obj[8]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[18]<=0.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0:
						# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>1:
							return 'False'
						elif obj[8]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[20]<=1:
				# {"feature": "Temperature", "instances": 39, "metric_value": 0.6194, "depth": 4}
				if obj[3]>55:
					# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Education", "instances": 18, "metric_value": 0.5033, "depth": 6}
						if obj[11]<=3:
							return 'True'
						elif obj[11]>3:
							# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[13]<=2:
								return 'False'
							elif obj[13]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[12]>1:
							return 'False'
						elif obj[12]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=55:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>0:
			# {"feature": "Time", "instances": 75, "metric_value": 0.9937, "depth": 3}
			if obj[4]<=1:
				# {"feature": "Restaurantlessthan20", "instances": 65, "metric_value": 0.9998, "depth": 4}
				if obj[17]>1.0:
					# {"feature": "Restaurant20to50", "instances": 52, "metric_value": 0.9904, "depth": 5}
					if obj[18]>0.0:
						# {"feature": "Coupon_validity", "instances": 47, "metric_value": 0.9997, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Age", "instances": 28, "metric_value": 0.9403, "depth": 7}
							if obj[8]<=6:
								# {"feature": "Temperature", "instances": 25, "metric_value": 0.8555, "depth": 8}
								if obj[3]>30:
									# {"feature": "Education", "instances": 20, "metric_value": 0.6098, "depth": 9}
									if obj[11]>1:
										return 'True'
									elif obj[11]<=1:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[20]<=1:
											# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 11}
											if obj[12]<=7:
												return 'True'
											elif obj[12]>7:
												# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]>0:
													return 'False'
												elif obj[5]<=0:
													return 'True'
												else: return 'True'
											else: return 'False'
										elif obj[20]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[3]<=30:
									# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]<=3:
										return 'False'
									elif obj[5]>3:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>6:
								return 'False'
							else: return 'False'
						elif obj[6]>0:
							# {"feature": "Bar", "instances": 19, "metric_value": 0.8315, "depth": 7}
							if obj[14]<=1.0:
								# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 8}
								if obj[5]>1:
									# {"feature": "Age", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[8]>2:
										# {"feature": "Temperature", "instances": 6, "metric_value": 1.0, "depth": 10}
										if obj[3]>30:
											# {"feature": "Maritalstatus", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[9]<=0:
												return 'False'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[3]<=30:
											return 'True'
										else: return 'True'
									elif obj[8]<=2:
										return 'False'
									else: return 'False'
								elif obj[5]<=1:
									return 'True'
								else: return 'True'
							elif obj[14]>1.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[18]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[17]<=1.0:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[5]<=1:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[12]>1:
							# {"feature": "Temperature", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]>30:
								return 'False'
							elif obj[3]<=30:
								return 'True'
							else: return 'True'
						elif obj[12]<=1:
							return 'True'
						else: return 'True'
					elif obj[5]>1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>1:
				# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[13]>0:
					return 'False'
				elif obj[13]<=0:
					# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[16]<=0.0:
		return 'False'
	else: return 'False'
