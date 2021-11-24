def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Direction_same", "instances": 85, "metric_value": 0.9975, "depth": 1}
	if obj[15]<=0:
		# {"feature": "Coupon", "instances": 64, "metric_value": 0.9937, "depth": 2}
		if obj[3]>0:
			# {"feature": "Time", "instances": 52, "metric_value": 0.9989, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Age", "instances": 27, "metric_value": 0.951, "depth": 4}
				if obj[6]>3:
					# {"feature": "Income", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[11]<=6:
						# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.8631, "depth": 6}
						if obj[13]>1.0:
							return 'True'
						elif obj[13]<=1.0:
							# {"feature": "Maritalstatus", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[7]>1:
								return 'False'
							elif obj[7]<=1:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[11]>6:
						return 'False'
					else: return 'False'
				elif obj[6]<=3:
					return 'False'
				else: return 'False'
			elif obj[2]>1:
				# {"feature": "Occupation", "instances": 25, "metric_value": 0.9044, "depth": 4}
				if obj[10]>4:
					# {"feature": "Weather", "instances": 18, "metric_value": 0.9911, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 6}
						if obj[9]>0:
							# {"feature": "Gender", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								# {"feature": "Maritalstatus", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[13]<=0.0:
										return 'True'
									elif obj[13]>0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[5]>0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[0]>0:
									return 'True'
								elif obj[0]<=0:
									# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6]>0:
										return 'False'
									elif obj[6]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							else: return 'True'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				elif obj[10]<=4:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]<=0:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[12]<=1.0:
				return 'False'
			elif obj[12]>1.0:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[15]>0:
		# {"feature": "Gender", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[5]<=0:
			return 'True'
		elif obj[5]>0:
			# {"feature": "Coupon_validity", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Children", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=0:
						return 'True'
					elif obj[8]>0:
						return 'False'
					else: return 'False'
				elif obj[6]>4:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
