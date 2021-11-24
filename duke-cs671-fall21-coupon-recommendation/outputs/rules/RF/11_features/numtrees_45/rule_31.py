def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 15, "metric_value": 0.9183, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[7]>0.0:
				# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]>0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>1:
						return 'True'
					elif obj[2]<=1:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]<=0:
						return 'False'
					elif obj[9]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[6]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
