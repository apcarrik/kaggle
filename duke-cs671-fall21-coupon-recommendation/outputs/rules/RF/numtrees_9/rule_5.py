def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Age", "instances": 113, "metric_value": 0.9954, "depth": 1}
	if obj[8]>3:
		# {"feature": "Carryaway", "instances": 61, "metric_value": 0.9127, "depth": 2}
		if obj[16]<=3.0:
			# {"feature": "Driving_to", "instances": 58, "metric_value": 0.8727, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon_validity", "instances": 46, "metric_value": 0.7554, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Time", "instances": 27, "metric_value": 0.5033, "depth": 5}
					if obj[4]<=1:
						return 'True'
					elif obj[4]>1:
						# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[5]>0:
							# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[9]<=1:
								return 'True'
							elif obj[9]>1:
								return 'False'
							else: return 'False'
						elif obj[5]<=0:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[11]<=2:
								return 'False'
							elif obj[11]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[6]>0:
					# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[13]>3:
						# {"feature": "Time", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[4]>0:
							# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[5]>2:
								# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[15]<=2.0:
									# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[20]<=1:
										# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[11]<=0:
											return 'True'
										elif obj[11]>0:
											return 'False'
										else: return 'False'
									elif obj[20]>1:
										return 'False'
									else: return 'False'
								elif obj[15]>2.0:
									return 'True'
								else: return 'True'
							elif obj[5]<=2:
								return 'False'
							else: return 'False'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[13]<=3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Temperature", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]<=55:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[14]<=2.0:
						return 'True'
					elif obj[14]>2.0:
						return 'False'
					else: return 'False'
				elif obj[3]>55:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[16]>3.0:
			return 'False'
		else: return 'False'
	elif obj[8]<=3:
		# {"feature": "Weather", "instances": 52, "metric_value": 0.9612, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Passanger", "instances": 37, "metric_value": 0.9995, "depth": 3}
			if obj[1]>0:
				# {"feature": "Maritalstatus", "instances": 33, "metric_value": 0.9834, "depth": 4}
				if obj[9]>0:
					# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[11]<=2:
						# {"feature": "Time", "instances": 13, "metric_value": 0.3912, "depth": 6}
						if obj[4]<=3:
							return 'True'
						elif obj[4]>3:
							# {"feature": "Temperature", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>55:
								return 'False'
							elif obj[3]<=55:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[11]>2:
						# {"feature": "Children", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[10]<=0:
							return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[9]<=0:
					# {"feature": "Time", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[4]>1:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[5]>1:
							# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[6]<=0:
								return 'True'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[14]<=0.0:
									return 'False'
								elif obj[14]>0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[5]<=1:
							return 'False'
						else: return 'False'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>0:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 3}
			if obj[12]>1:
				return 'False'
			elif obj[12]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
