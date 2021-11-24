def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[4]<=8:
		# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[6]<=2.0:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[7]>0.0:
				return 'True'
			elif obj[7]<=0.0:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2.0:
			return 'False'
		else: return 'False'
	elif obj[4]>8:
		# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
