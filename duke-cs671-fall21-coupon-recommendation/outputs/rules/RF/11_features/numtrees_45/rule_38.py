def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[4]>0:
			# {"feature": "Passanger", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[0]>1:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=3:
					return 'True'
				elif obj[2]>3:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=1:
				# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[7]<=3.0:
					return 'False'
				elif obj[7]>3.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
