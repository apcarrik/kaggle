def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Income", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[12]>1:
		# {"feature": "Coupon", "instances": 67, "metric_value": 0.9869, "depth": 2}
		if obj[4]>1:
			# {"feature": "Time", "instances": 52, "metric_value": 0.9471, "depth": 3}
			if obj[3]>1:
				# {"feature": "Bar", "instances": 28, "metric_value": 0.7496, "depth": 4}
				if obj[13]<=1.0:
					# {"feature": "Maritalstatus", "instances": 22, "metric_value": 0.5746, "depth": 5}
					if obj[8]<=2:
						# {"feature": "Education", "instances": 21, "metric_value": 0.4537, "depth": 6}
						if obj[10]<=2:
							return 'True'
						elif obj[10]>2:
							# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[11]>6:
								return 'True'
							elif obj[11]<=6:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[18]>1:
									return 'False'
								elif obj[18]<=1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[8]>2:
						return 'False'
					else: return 'False'
				elif obj[13]>1.0:
					# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[6]>0:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]<=2:
							return 'True'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=1:
				# {"feature": "Restaurantlessthan20", "instances": 24, "metric_value": 0.995, "depth": 4}
				if obj[15]<=3.0:
					# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 5}
					if obj[11]<=9:
						# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[14]>0.0:
							return 'True'
						elif obj[14]<=0.0:
							# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>9:
						# {"feature": "Temperature", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]<=55:
							return 'False'
						elif obj[2]>55:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[15]>3.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]<=1:
			# {"feature": "Temperature", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[2]>55:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[16]<=1.0:
					# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[8]<=1:
							return 'False'
						elif obj[8]>1:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						return 'False'
					else: return 'False'
				elif obj[16]>1.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=55:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[12]<=1:
		# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[10]<=2:
			# {"feature": "Coupon", "instances": 12, "metric_value": 0.4138, "depth": 3}
			if obj[4]>1:
				return 'False'
			elif obj[4]<=1:
				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>2:
			# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[11]>1:
					return 'False'
				elif obj[11]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
