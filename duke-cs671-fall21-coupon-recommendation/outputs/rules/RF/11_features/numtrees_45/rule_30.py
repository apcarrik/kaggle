def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[5]<=7:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[10]>1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]>3:
					# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[8]>1.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=1:
							return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					elif obj[8]<=1.0:
						return 'True'
					else: return 'True'
				elif obj[3]<=3:
					return 'False'
				else: return 'False'
			elif obj[10]<=1:
				return 'True'
			else: return 'True'
		elif obj[5]>7:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
