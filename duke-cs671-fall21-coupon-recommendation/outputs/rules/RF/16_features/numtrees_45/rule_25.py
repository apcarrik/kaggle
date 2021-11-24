def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[13]>0.0:
		# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[15]>1:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[10]<=3:
					return 'False'
				elif obj[10]>3:
					# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							return 'True'
						elif obj[2]>0:
							return 'False'
						else: return 'False'
					elif obj[1]>0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[5]<=0:
					return 'True'
				elif obj[5]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]<=1:
			return 'True'
		else: return 'True'
	elif obj[13]<=0.0:
		return 'False'
	else: return 'False'
