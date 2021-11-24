def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Time", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=0:
			return 'True'
		elif obj[1]>0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[5]>4:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=3:
						return 'True'
					elif obj[4]>3:
						return 'False'
					else: return 'False'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[5]<=4:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=3:
					return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			elif obj[7]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
