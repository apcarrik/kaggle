def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Income", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]>0:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[15]>1:
			# {"feature": "Coffeehouse", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=0:
					return 'True'
				elif obj[4]>0:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]>2.0:
				return 'False'
			else: return 'False'
		elif obj[15]<=1:
			return 'True'
		else: return 'True'
	elif obj[10]<=0:
		# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[6]>0:
			return 'False'
		elif obj[6]<=0:
			# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
