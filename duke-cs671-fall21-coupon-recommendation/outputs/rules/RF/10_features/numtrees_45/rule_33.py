def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[5]<=1.0:
		# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[3]>1:
			return 'True'
		elif obj[3]<=1:
			# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[5]>1.0:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[4]>4:
				return 'False'
			elif obj[4]<=4:
				# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
