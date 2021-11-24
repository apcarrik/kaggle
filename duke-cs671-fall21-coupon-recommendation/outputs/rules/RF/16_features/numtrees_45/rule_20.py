def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=3:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[12]>0.0:
			# {"feature": "Age", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[6]<=4:
				# {"feature": "Coupon_validity", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[2]<=1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					elif obj[2]>1:
						return 'True'
					else: return 'True'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			elif obj[6]>4:
				return 'True'
			else: return 'True'
		elif obj[12]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[10]>3:
		return 'True'
	else: return 'True'
