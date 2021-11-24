def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[3]>4:
			# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[5]>0.0:
				return 'False'
			elif obj[5]<=0.0:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>3:
					return 'True'
				elif obj[1]<=3:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=4:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
