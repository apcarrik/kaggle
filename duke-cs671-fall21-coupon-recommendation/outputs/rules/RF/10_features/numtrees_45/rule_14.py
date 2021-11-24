def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[4]<=6:
				# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=0.0:
					return 'False'
				elif obj[6]>0.0:
					# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0.0:
						return 'True'
					elif obj[5]>0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]>6:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[5]>0.0:
			return 'False'
		elif obj[5]<=0.0:
			# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[9]<=1:
				return 'True'
			elif obj[9]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
