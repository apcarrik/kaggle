def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Income", "instances": 82, "metric_value": 0.9961, "depth": 2}
		if obj[13]>0:
			# {"feature": "Coupon", "instances": 67, "metric_value": 0.9727, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Age", "instances": 44, "metric_value": 1.0, "depth": 4}
				if obj[8]<=5:
					# {"feature": "Direction_same", "instances": 39, "metric_value": 0.9881, "depth": 5}
					if obj[19]<=0:
						# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.8905, "depth": 6}
						if obj[15]>0.0:
							# {"feature": "Occupation", "instances": 22, "metric_value": 0.9457, "depth": 7}
							if obj[12]<=5:
								# {"feature": "Time", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[4]<=1:
									# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[20]<=2:
										return 'False'
									elif obj[20]>2:
										# {"feature": "Weather", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[2]>0:
											# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=30:
												return 'True'
											elif obj[3]>30:
												return 'False'
											else: return 'False'
										elif obj[2]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[4]>1:
									return 'True'
								else: return 'True'
							elif obj[12]>5:
								# {"feature": "Carryaway", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[16]>2.0:
									return 'False'
								elif obj[16]<=2.0:
									# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[2]>0:
										return 'True'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[15]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[19]>0:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[12]<=6:
							# {"feature": "Driving_to", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[15]>1.0:
									return 'True'
								elif obj[15]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[12]>6:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[8]>5:
					return 'True'
				else: return 'True'
			elif obj[5]>3:
				# {"feature": "Carryaway", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[16]<=2.0:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[14]<=2.0:
						# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[9]<=1:
							return 'False'
						elif obj[9]>1:
							# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[8]>0:
								# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12]>1:
									return 'True'
								elif obj[12]<=1:
									return 'False'
								else: return 'False'
							elif obj[8]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]>2.0:
						return 'True'
					else: return 'True'
				elif obj[16]>2.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[13]<=0:
			# {"feature": "Weather", "instances": 15, "metric_value": 0.8366, "depth": 3}
			if obj[2]<=0:
				# {"feature": "Driving_to", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3]>55:
						return 'False'
					elif obj[3]<=55:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>1:
		# {"feature": "Restaurant20to50", "instances": 45, "metric_value": 0.8366, "depth": 2}
		if obj[18]<=1.0:
			# {"feature": "Coupon_validity", "instances": 33, "metric_value": 0.9457, "depth": 3}
			if obj[6]<=0:
				# {"feature": "Coupon", "instances": 18, "metric_value": 0.65, "depth": 4}
				if obj[5]>0:
					# {"feature": "Maritalstatus", "instances": 15, "metric_value": 0.3534, "depth": 5}
					if obj[9]<=1:
						return 'True'
					elif obj[9]>1:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[12]<=6:
							return 'False'
						elif obj[12]>6:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]>0:
						return 'False'
					elif obj[11]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]>0:
				# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[4]>0:
					# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[8]>0:
						return 'False'
					elif obj[8]<=0:
						# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[10]>0:
							return 'True'
						elif obj[10]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]<=0:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[11]<=2:
						return 'True'
					elif obj[11]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[18]>1.0:
			return 'True'
		else: return 'True'
	else: return 'True'
