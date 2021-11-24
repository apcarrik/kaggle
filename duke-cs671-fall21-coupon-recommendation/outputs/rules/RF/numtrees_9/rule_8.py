def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Driving_to", "instances": 113, "metric_value": 0.9999, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Education", "instances": 85, "metric_value": 0.9774, "depth": 2}
		if obj[11]<=3:
			# {"feature": "Restaurantlessthan20", "instances": 78, "metric_value": 0.9924, "depth": 3}
			if obj[17]<=2.0:
				# {"feature": "Coffeehouse", "instances": 44, "metric_value": 0.9257, "depth": 4}
				if obj[15]<=2.0:
					# {"feature": "Age", "instances": 37, "metric_value": 0.974, "depth": 5}
					if obj[8]>3:
						# {"feature": "Income", "instances": 20, "metric_value": 0.8113, "depth": 6}
						if obj[13]<=3:
							# {"feature": "Passanger", "instances": 10, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								# {"feature": "Carryaway", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[16]<=2.0:
									# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[2]<=0:
										return 'True'
									elif obj[2]>0:
										return 'False'
									else: return 'False'
								elif obj[16]>2.0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[13]>3:
							return 'True'
						else: return 'True'
					elif obj[8]<=3:
						# {"feature": "Children", "instances": 17, "metric_value": 0.9774, "depth": 6}
						if obj[10]>0:
							# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[1]<=1:
										# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]<=1:
											return 'True'
										elif obj[2]>1:
											return 'False'
										else: return 'False'
									elif obj[1]>1:
										return 'False'
									else: return 'False'
								elif obj[9]>0:
									return 'True'
								else: return 'True'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						elif obj[10]<=0:
							# {"feature": "Carryaway", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[16]<=2.0:
								return 'False'
							elif obj[16]>2.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[15]>2.0:
					return 'True'
				else: return 'True'
			elif obj[17]>2.0:
				# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 4}
				if obj[12]>1:
					# {"feature": "Gender", "instances": 30, "metric_value": 0.9183, "depth": 5}
					if obj[7]>0:
						# {"feature": "Coupon", "instances": 19, "metric_value": 0.6292, "depth": 6}
						if obj[5]<=2:
							return 'False'
						elif obj[5]>2:
							# {"feature": "Coupon_validity", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[6]>0:
								return 'False'
							elif obj[6]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=0:
						# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[5]<=3:
							return 'True'
						elif obj[5]>3:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]<=2:
								return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[12]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[11]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Time", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9774, "depth": 3}
			if obj[15]>0.0:
				# {"feature": "Temperature", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[3]>55:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[12]>3:
							return 'False'
						elif obj[12]<=3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=55:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[12]<=11:
						return 'False'
					elif obj[12]>11:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[15]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[4]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
