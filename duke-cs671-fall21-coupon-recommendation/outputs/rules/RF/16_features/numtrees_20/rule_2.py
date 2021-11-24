def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[3]>1:
		# {"feature": "Time", "instances": 34, "metric_value": 0.9082, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[6]<=5:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[0]>0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[9]>2:
						# {"feature": "Income", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[10]<=7:
							# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[15]<=1:
								# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[11]>0.0:
									# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=2:
										return 'True'
									elif obj[8]>2:
										return 'False'
									else: return 'False'
								elif obj[11]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[15]>1:
								return 'True'
							else: return 'True'
						elif obj[10]>7:
							return 'False'
						else: return 'False'
					elif obj[9]<=2:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]>5:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			# {"feature": "Education", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[8]<=2:
				return 'True'
			elif obj[8]>2:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[0]>1:
					# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[9]<=16:
						return 'False'
					elif obj[9]>16:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Income", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[10]>3:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[9]>1:
				return 'False'
			elif obj[9]<=1:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]<=3:
			# {"feature": "Weather", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[1]>0:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]>0:
					return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
