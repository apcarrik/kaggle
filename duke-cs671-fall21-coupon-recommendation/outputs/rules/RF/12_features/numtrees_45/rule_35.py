def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Bar", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[7]<=1.0:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[2]>0:
			# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				# {"feature": "Passanger", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]>1:
					# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>0:
						# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]>0.0:
							return 'False'
						elif obj[8]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[7]>1.0:
		return 'True'
	else: return 'True'
