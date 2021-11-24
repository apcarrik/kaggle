def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Coupon", "instances": 113, "metric_value": 0.9904, "depth": 1}
	if obj[5]>1:
		# {"feature": "Passanger", "instances": 82, "metric_value": 0.9373, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon_validity", "instances": 61, "metric_value": 0.9951, "depth": 3}
			if obj[6]>0:
				# {"feature": "Coffeehouse", "instances": 33, "metric_value": 0.9183, "depth": 4}
				if obj[15]>0.0:
					# {"feature": "Carryaway", "instances": 27, "metric_value": 0.9751, "depth": 5}
					if obj[16]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9183, "depth": 6}
						if obj[18]<=1.0:
							# {"feature": "Maritalstatus", "instances": 16, "metric_value": 0.6962, "depth": 7}
							if obj[9]>0:
								return 'False'
							elif obj[9]<=0:
								# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[12]<=9:
									# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										return 'True'
									else: return 'True'
								elif obj[12]>9:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[18]>1.0:
							# {"feature": "Driving_to", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]>2:
									# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]<=2:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[16]>3.0:
						return 'True'
					else: return 'True'
				elif obj[15]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[6]<=0:
				# {"feature": "Age", "instances": 28, "metric_value": 0.7496, "depth": 4}
				if obj[8]<=3:
					# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[13]<=3:
						# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[12]>4:
							return 'False'
						elif obj[12]<=4:
							# {"feature": "Maritalstatus", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[9]<=1:
								return 'True'
							elif obj[9]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[13]>3:
						return 'True'
					else: return 'True'
				elif obj[8]>3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.2762, "depth": 3}
			if obj[12]>0:
				return 'True'
			elif obj[12]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[5]<=1:
		# {"feature": "Time", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[4]>1:
			# {"feature": "Restaurantlessthan20", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[17]>1.0:
				# {"feature": "Income", "instances": 17, "metric_value": 0.3228, "depth": 4}
				if obj[13]<=6:
					return 'False'
				elif obj[13]>6:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[11]<=0:
						return 'False'
					elif obj[11]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[17]<=1.0:
				return 'True'
			else: return 'True'
		elif obj[4]<=1:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[14]<=0.0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[8]>1:
					return 'False'
				elif obj[8]<=1:
					return 'True'
				else: return 'True'
			elif obj[14]>0.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
