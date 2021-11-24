def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Restaurantlessthan20, obj[17]: Restaurant20to50, obj[18]: Direction_same, obj[19]: Distance
	# {"feature": "Coupon_validity", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Restaurant20to50", "instances": 72, "metric_value": 0.9038, "depth": 2}
		if obj[17]>-1.0:
			# {"feature": "Bar", "instances": 69, "metric_value": 0.8685, "depth": 3}
			if obj[14]<=1.0:
				# {"feature": "Education", "instances": 40, "metric_value": 0.9837, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Restaurantlessthan20", "instances": 31, "metric_value": 0.9072, "depth": 5}
					if obj[16]>1.0:
						# {"feature": "Coupon", "instances": 26, "metric_value": 0.9612, "depth": 6}
						if obj[5]>0:
							# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 7}
							if obj[8]>2:
								# {"feature": "Temperature", "instances": 15, "metric_value": 0.9968, "depth": 8}
								if obj[3]>55:
									# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.9799, "depth": 9}
									if obj[15]<=2.0:
										# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[12]<=19:
											# {"feature": "Income", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[13]>3:
												# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[10]>0:
													# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[4]<=2:
														return 'True'
													elif obj[4]>2:
														return 'False'
													else: return 'False'
												elif obj[10]<=0:
													return 'False'
												else: return 'False'
											elif obj[13]<=3:
												return 'False'
											else: return 'False'
										elif obj[12]>19:
											return 'True'
										else: return 'True'
									elif obj[15]>2.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=55:
									return 'True'
								else: return 'True'
							elif obj[8]<=2:
								return 'True'
							else: return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					elif obj[16]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[11]>2:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[15]>0.0:
						return 'False'
					elif obj[15]<=0.0:
						# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[5]>0:
							return 'True'
						elif obj[5]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[14]>1.0:
				# {"feature": "Passanger", "instances": 29, "metric_value": 0.4798, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 18, "metric_value": 0.65, "depth": 5}
					if obj[5]<=3:
						# {"feature": "Driving_to", "instances": 17, "metric_value": 0.5226, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[18]>0:
								return 'True'
							elif obj[18]<=0:
								# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>30:
									return 'False'
								elif obj[3]<=30:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[5]>3:
						return 'False'
					else: return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[17]<=-1.0:
			return 'False'
		else: return 'False'
	elif obj[6]>0:
		# {"feature": "Coupon", "instances": 55, "metric_value": 0.9806, "depth": 2}
		if obj[5]>1:
			# {"feature": "Occupation", "instances": 49, "metric_value": 0.9973, "depth": 3}
			if obj[12]>5:
				# {"feature": "Education", "instances": 27, "metric_value": 0.8767, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Income", "instances": 21, "metric_value": 0.9587, "depth": 5}
					if obj[13]>0:
						# {"feature": "Age", "instances": 18, "metric_value": 0.9911, "depth": 6}
						if obj[8]<=4:
							# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[1]>0:
								# {"feature": "Restaurantlessthan20", "instances": 13, "metric_value": 0.8905, "depth": 8}
								if obj[16]>1.0:
									# {"feature": "Driving_to", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Temperature", "instances": 9, "metric_value": 0.5033, "depth": 10}
										if obj[3]<=55:
											return 'False'
										elif obj[3]>55:
											# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[10]>0:
												return 'False'
											elif obj[10]<=0:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[16]<=1.0:
									# {"feature": "Driving_to", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=1:
										return 'True'
									elif obj[0]>1:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[8]>4:
							# {"feature": "Restaurantlessthan20", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[16]<=2.0:
								return 'True'
							elif obj[16]>2.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]>2:
					return 'False'
				else: return 'False'
			elif obj[12]<=5:
				# {"feature": "Driving_to", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Distance", "instances": 17, "metric_value": 0.6723, "depth": 5}
					if obj[19]>1:
						# {"feature": "Weather", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[8]>0:
									return 'False'
								elif obj[8]<=0:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[11]>2:
										return 'True'
									elif obj[11]<=2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>2:
								return 'True'
							else: return 'True'
						elif obj[2]>1:
							return 'True'
						else: return 'True'
					elif obj[19]<=1:
						return 'True'
					else: return 'True'
				elif obj[0]>1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[11]<=3:
						return 'False'
					elif obj[11]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[5]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
