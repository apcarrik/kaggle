def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[5]>2:
			# {"feature": "Bar", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[6]>0.0:
				# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[10]>1:
						return 'True'
					elif obj[10]<=1:
						# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0]<=0:
							return 'True'
						elif obj[0]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			elif obj[6]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[5]<=2:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
