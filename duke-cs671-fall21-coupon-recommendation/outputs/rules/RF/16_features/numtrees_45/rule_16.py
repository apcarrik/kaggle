def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]>1:
		# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]>0:
				# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[12]<=2.0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]>1:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0:
								# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									return 'False'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				elif obj[12]>2.0:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[13]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[6]<=1:
		return 'True'
	else: return 'True'
