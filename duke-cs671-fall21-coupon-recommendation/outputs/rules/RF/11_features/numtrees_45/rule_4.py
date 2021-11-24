def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[4]>1:
				# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=3:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5]<=16:
						return 'True'
					elif obj[5]>16:
						return 'False'
					else: return 'False'
				elif obj[3]>3:
					return 'False'
				else: return 'False'
			elif obj[4]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
