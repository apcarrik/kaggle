def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[7]>0.0:
			# {"feature": "Time", "instances": 18, "metric_value": 0.3095, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[10]>1:
					return 'True'
				elif obj[10]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]<=0.0:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[8]>0.0:
				# {"feature": "Age", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]<=4:
					return 'False'
				elif obj[3]>4:
					# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]<=0.0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
