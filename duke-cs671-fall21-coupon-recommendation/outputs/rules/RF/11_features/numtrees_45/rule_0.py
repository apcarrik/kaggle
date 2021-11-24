def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[5]<=7:
				# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[3]<=3:
						return 'True'
					elif obj[3]>3:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[4]>1:
							return 'True'
						elif obj[4]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			elif obj[5]>7:
				# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
