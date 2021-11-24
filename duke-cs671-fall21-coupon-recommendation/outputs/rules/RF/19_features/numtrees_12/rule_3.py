def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Bar", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[13]<=0.0:
		# {"feature": "Coupon", "instances": 43, "metric_value": 0.9523, "depth": 2}
		if obj[4]>0:
			# {"feature": "Coffeehouse", "instances": 37, "metric_value": 0.8419, "depth": 3}
			if obj[14]<=3.0:
				# {"feature": "Income", "instances": 34, "metric_value": 0.7335, "depth": 4}
				if obj[12]>1:
					# {"feature": "Gender", "instances": 27, "metric_value": 0.5033, "depth": 5}
					if obj[6]<=0:
						return 'True'
					elif obj[6]>0:
						# {"feature": "Age", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[7]>1:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[16]>0.0:
								# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							elif obj[16]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[12]<=1:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[18]<=2:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[10]>0:
							return 'False'
						elif obj[10]<=0:
							return 'True'
						else: return 'True'
					elif obj[18]>2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[14]>3.0:
				return 'False'
			else: return 'False'
		elif obj[4]<=0:
			return 'False'
		else: return 'False'
	elif obj[13]>0.0:
		# {"feature": "Children", "instances": 42, "metric_value": 0.9737, "depth": 2}
		if obj[9]<=0:
			# {"feature": "Passanger", "instances": 28, "metric_value": 0.8113, "depth": 3}
			if obj[0]>0:
				# {"feature": "Occupation", "instances": 21, "metric_value": 0.4537, "depth": 4}
				if obj[11]<=7:
					# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[16]>-1.0:
							return 'False'
						elif obj[16]<=-1.0:
							# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=2:
								return 'False'
							elif obj[4]>2:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[11]>7:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[2]>30:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[11]>1:
						return 'True'
					elif obj[11]<=1:
						return 'False'
					else: return 'False'
				elif obj[2]<=30:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Age", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[7]<=2:
					# {"feature": "Temperature", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=55:
						return 'True'
					elif obj[2]>55:
						# {"feature": "Restaurantlessthan20", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[15]<=3.0:
							return 'False'
						elif obj[15]>3.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
