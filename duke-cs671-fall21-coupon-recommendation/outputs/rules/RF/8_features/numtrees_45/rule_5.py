def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=7:
		# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]<=2.0:
					return 'False'
				elif obj[4]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]>7:
		# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[7]<=2:
			return 'True'
		elif obj[7]>2:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
