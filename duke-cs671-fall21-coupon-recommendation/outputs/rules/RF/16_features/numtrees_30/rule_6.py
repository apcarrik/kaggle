def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Income", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[10]>3:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]<=1:
				# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				elif obj[4]>0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]<=0:
							return 'True'
						elif obj[1]>0:
							return 'False'
						else: return 'False'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>1:
				return 'False'
			else: return 'False'
		elif obj[10]<=3:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Income", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[10]>0:
			# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]<=0:
			# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]<=2:
				return 'False'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
