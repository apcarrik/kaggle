def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[9]<=12:
		# {"feature": "Income", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[10]>0:
			# {"feature": "Age", "instances": 27, "metric_value": 0.9751, "depth": 3}
			if obj[6]>0:
				# {"feature": "Coupon", "instances": 24, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[14]<=0:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[15]<=2:
									# {"feature": "Gender", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0]>1:
											return 'False'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[15]>2:
									return 'False'
								else: return 'False'
							elif obj[14]>0:
								return 'False'
							else: return 'False'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[3]<=0:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=3:
						return 'False'
					elif obj[8]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[6]<=0:
				return 'False'
			else: return 'False'
		elif obj[10]<=0:
			return 'True'
		else: return 'True'
	elif obj[9]>12:
		return 'False'
	else: return 'False'
