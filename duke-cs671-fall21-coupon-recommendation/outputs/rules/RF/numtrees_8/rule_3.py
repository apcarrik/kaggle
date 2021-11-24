def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 0.9621, "depth": 1}
	if obj[15]<=3.0:
		# {"feature": "Carryaway", "instances": 115, "metric_value": 0.9321, "depth": 2}
		if obj[16]>1.0:
			# {"feature": "Income", "instances": 88, "metric_value": 0.861, "depth": 3}
			if obj[13]<=6:
				# {"feature": "Age", "instances": 79, "metric_value": 0.9005, "depth": 4}
				if obj[8]<=3:
					# {"feature": "Maritalstatus", "instances": 42, "metric_value": 0.9852, "depth": 5}
					if obj[9]<=2:
						# {"feature": "Occupation", "instances": 40, "metric_value": 0.971, "depth": 6}
						if obj[12]<=11:
							# {"feature": "Time", "instances": 25, "metric_value": 0.9988, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 8}
								if obj[11]>0:
									# {"feature": "Temperature", "instances": 12, "metric_value": 1.0, "depth": 9}
									if obj[3]>55:
										# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9183, "depth": 10}
										if obj[6]>0:
											# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[5]<=1:
												# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 0.8113, "depth": 12}
												if obj[17]<=3.0:
													return 'True'
												elif obj[17]>3.0:
													return 'False'
												else: return 'False'
											elif obj[5]>1:
												return 'False'
											else: return 'False'
										elif obj[6]<=0:
											return 'True'
										else: return 'True'
									elif obj[3]<=55:
										return 'False'
									else: return 'False'
								elif obj[11]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>2:
								# {"feature": "Children", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[10]<=0:
									return 'False'
								elif obj[10]>0:
									# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]>0:
										return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'False'
						elif obj[12]>11:
							# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[6]>0:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[20]>1:
									# {"feature": "Driving_to", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[5]>1:
											# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[10]>0:
												return 'True'
											elif obj[10]<=0:
												# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]>2:
													return 'True'
												elif obj[11]<=2:
													return 'False'
												else: return 'False'
											else: return 'True'
										elif obj[5]<=1:
											return 'False'
										else: return 'False'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								elif obj[20]<=1:
									return 'True'
								else: return 'True'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[9]>2:
						return 'False'
					else: return 'False'
				elif obj[8]>3:
					# {"feature": "Coupon", "instances": 37, "metric_value": 0.6998, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9341, "depth": 6}
						if obj[18]>0.0:
							# {"feature": "Driving_to", "instances": 16, "metric_value": 0.8113, "depth": 7}
							if obj[0]>0:
								# {"feature": "Temperature", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[3]<=55:
									# {"feature": "Weather", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[2]>0:
										# {"feature": "Restaurantlessthan20", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[17]>1.0:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[7]<=0:
												return 'False'
											elif obj[7]>0:
												return 'True'
											else: return 'True'
										elif obj[17]<=1.0:
											return 'True'
										else: return 'True'
									elif obj[2]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>55:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[18]<=0.0:
							# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>0:
								return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[5]>2:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[13]>6:
				return 'True'
			else: return 'True'
		elif obj[16]<=1.0:
			# {"feature": "Education", "instances": 27, "metric_value": 0.9911, "depth": 3}
			if obj[11]<=3:
				# {"feature": "Weather", "instances": 24, "metric_value": 0.9544, "depth": 4}
				if obj[2]<=1:
					# {"feature": "Coupon", "instances": 22, "metric_value": 0.9024, "depth": 5}
					if obj[5]>1:
						# {"feature": "Passanger", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[1]>0:
							# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[4]<=2:
								# {"feature": "Restaurantlessthan20", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[17]<=2.0:
									# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										# {"feature": "Driving_to", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]<=0:
											return 'True'
										elif obj[0]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[17]>2.0:
									return 'True'
								else: return 'True'
							elif obj[4]>2:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[5]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]>1:
					return 'True'
				else: return 'True'
			elif obj[11]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]>3.0:
		# {"feature": "Carryaway", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[16]<=3.0:
			return 'False'
		elif obj[16]>3.0:
			# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
