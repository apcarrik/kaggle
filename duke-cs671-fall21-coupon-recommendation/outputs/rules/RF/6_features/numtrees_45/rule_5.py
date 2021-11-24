def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=7:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[1]>0:
			# {"feature": "Passanger", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=2:
					return 'True'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]>0.0:
					return 'True'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>7:
		return 'False'
	else: return 'False'
