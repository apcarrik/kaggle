def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Distance", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[5]<=0:
				return 'True'
			elif obj[5]>0:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=4:
					return 'True'
				elif obj[3]>4:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
