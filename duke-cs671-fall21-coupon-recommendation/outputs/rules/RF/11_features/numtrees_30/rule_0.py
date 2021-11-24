def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[9]<=0:
		# {"feature": "Bar", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[6]<=2.0:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.9957, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[5]>1:
					# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[1]>1:
						return 'False'
					elif obj[1]<=1:
						# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=4:
						return 'False'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2.0:
			return 'False'
		else: return 'False'
	elif obj[9]>0:
		return 'True'
	else: return 'True'
