def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[7]>0.0:
				return 'False'
			elif obj[7]<=0.0:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[10]<=1:
					return 'False'
				elif obj[10]>1:
					# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[9]<=0:
						return 'True'
					elif obj[9]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[2]>3:
			# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[7]>1.0:
				return 'True'
			elif obj[7]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
