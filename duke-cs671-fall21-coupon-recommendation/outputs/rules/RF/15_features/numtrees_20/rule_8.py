def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 41, "metric_value": 0.9996, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.9812, "depth": 3}
			if obj[8]<=6:
				# {"feature": "Distance", "instances": 18, "metric_value": 0.9911, "depth": 4}
				if obj[14]<=2:
					# {"feature": "Income", "instances": 14, "metric_value": 0.9852, "depth": 5}
					if obj[9]<=3:
						# {"feature": "Children", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[1]>0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[7]>0:
									return 'False'
								elif obj[7]<=0:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[12]>0.0:
										return 'True'
									elif obj[12]<=0.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[9]>3:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>1:
							return 'True'
						elif obj[1]<=1:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[14]>2:
					return 'True'
				else: return 'True'
			elif obj[8]>6:
				# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[7]>1:
						return 'True'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[7]<=1:
				return 'True'
			elif obj[7]>1:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[3]<=0:
			return 'False'
		elif obj[3]>0:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
