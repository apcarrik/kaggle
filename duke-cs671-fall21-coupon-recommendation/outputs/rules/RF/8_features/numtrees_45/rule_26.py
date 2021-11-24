def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[3]>5:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[5]<=1.0:
				return 'False'
			elif obj[5]>1.0:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>1.0:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]<=2:
				return 'True'
			elif obj[7]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=5:
		return 'True'
	else: return 'True'
