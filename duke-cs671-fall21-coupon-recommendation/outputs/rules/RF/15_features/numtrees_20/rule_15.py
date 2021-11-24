def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[11]<=3.0:
		# {"feature": "Gender", "instances": 45, "metric_value": 0.9968, "depth": 2}
		if obj[4]>0:
			# {"feature": "Distance", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[14]>1:
				# {"feature": "Age", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[5]>0:
					# {"feature": "Passanger", "instances": 13, "metric_value": 0.9612, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 6}
						if obj[1]<=3:
							# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[8]<=8:
								# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[2]<=0:
									# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[9]>0:
										return 'False'
									elif obj[9]<=0:
										return 'True'
									else: return 'True'
								elif obj[2]>0:
									return 'True'
								else: return 'True'
							elif obj[8]>8:
								return 'False'
							else: return 'False'
						elif obj[1]>3:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					return 'False'
				else: return 'False'
			elif obj[14]<=1:
				# {"feature": "Income", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[9]<=6:
					return 'True'
				elif obj[9]>6:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=0:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[8]<=7:
				# {"feature": "Income", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[9]<=6:
					# {"feature": "Age", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[5]>3:
						# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[7]>0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							return 'False'
						else: return 'False'
					elif obj[5]<=3:
						return 'False'
					else: return 'False'
				elif obj[9]>6:
					return 'True'
				else: return 'True'
			elif obj[8]>7:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[11]>3.0:
		return 'False'
	else: return 'False'
