def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon_validity", "instances": 170, "metric_value": 0.99, "depth": 1}
	if obj[6]<=0:
		# {"feature": "Passanger", "instances": 94, "metric_value": 0.9035, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Coupon", "instances": 62, "metric_value": 0.9932, "depth": 3}
			if obj[5]>1:
				# {"feature": "Occupation", "instances": 36, "metric_value": 0.8524, "depth": 4}
				if obj[12]<=18:
					# {"feature": "Income", "instances": 33, "metric_value": 0.7455, "depth": 5}
					if obj[13]<=6:
						# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.8404, "depth": 6}
						if obj[15]<=2.0:
							# {"feature": "Distance", "instances": 21, "metric_value": 0.9183, "depth": 7}
							if obj[20]<=1:
								# {"feature": "Driving_to", "instances": 15, "metric_value": 0.7219, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[8]>1:
										# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[11]>0:
											return 'False'
										elif obj[11]<=0:
											return 'True'
										else: return 'True'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[20]>1:
								# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[9]<=1:
									return 'False'
								elif obj[9]>1:
									# {"feature": "Temperature", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>55:
										return 'True'
									elif obj[3]<=55:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[15]>2.0:
							return 'True'
						else: return 'True'
					elif obj[13]>6:
						return 'True'
					else: return 'True'
				elif obj[12]>18:
					return 'False'
				else: return 'False'
			elif obj[5]<=1:
				# {"feature": "Bar", "instances": 26, "metric_value": 0.8905, "depth": 4}
				if obj[14]>0.0:
					# {"feature": "Children", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[10]<=0:
						# {"feature": "Income", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[13]<=6:
							# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 7}
							if obj[15]<=3.0:
								# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[18]<=1.0:
									# {"feature": "Weather", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[2]>0:
										# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[12]<=6:
											return 'True'
										elif obj[12]>6:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8]>1:
												return 'False'
											elif obj[8]<=1:
												return 'True'
											else: return 'True'
										else: return 'False'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								elif obj[18]>1.0:
									return 'True'
								else: return 'True'
							elif obj[15]>3.0:
								return 'False'
							else: return 'False'
						elif obj[13]>6:
							return 'False'
						else: return 'False'
					elif obj[10]>0:
						return 'False'
					else: return 'False'
				elif obj[14]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>1:
			# {"feature": "Coupon", "instances": 32, "metric_value": 0.3373, "depth": 3}
			if obj[5]<=3:
				return 'True'
			elif obj[5]>3:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[18]>0.0:
					# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[12]<=7:
						return 'True'
					elif obj[12]>7:
						# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[20]<=1:
							return 'False'
						elif obj[20]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[18]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[6]>0:
		# {"feature": "Carryaway", "instances": 76, "metric_value": 0.9754, "depth": 2}
		if obj[16]>1.0:
			# {"feature": "Income", "instances": 61, "metric_value": 0.9983, "depth": 3}
			if obj[13]>3:
				# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9597, "depth": 4}
				if obj[19]<=0:
					# {"feature": "Restaurantlessthan20", "instances": 30, "metric_value": 0.9871, "depth": 5}
					if obj[17]>0.0:
						# {"feature": "Coffeehouse", "instances": 27, "metric_value": 0.999, "depth": 6}
						if obj[15]>0.0:
							# {"feature": "Temperature", "instances": 24, "metric_value": 0.9799, "depth": 7}
							if obj[3]<=55:
								# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[8]<=3:
									# {"feature": "Children", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[10]>0:
										# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[4]<=2:
											return 'True'
										elif obj[4]>2:
											# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=0:
												return 'True'
											elif obj[5]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[10]<=0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[1]>0:
											return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[8]>3:
									return 'False'
								else: return 'False'
							elif obj[3]>55:
								# {"feature": "Bar", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[14]<=2.0:
									return 'True'
								elif obj[14]>2.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[15]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[17]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[19]>0:
					return 'True'
				else: return 'True'
			elif obj[13]<=3:
				# {"feature": "Driving_to", "instances": 27, "metric_value": 0.8767, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurantlessthan20", "instances": 20, "metric_value": 0.971, "depth": 5}
					if obj[17]<=3.0:
						# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[15]<=2.0:
							# {"feature": "Distance", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[20]>1:
								# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[8]<=2:
									return 'False'
								elif obj[8]>2:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[20]<=1:
								return 'True'
							else: return 'True'
						elif obj[15]>2.0:
							return 'True'
						else: return 'True'
					elif obj[17]>3.0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[16]<=1.0:
			# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[9]<=1:
				return 'False'
			elif obj[9]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
