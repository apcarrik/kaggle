def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>1:
		# {"feature": "Passanger", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6]>0.0:
						return 'False'
					elif obj[6]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
