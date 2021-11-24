def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[8]<=3.0:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 3}
			if obj[5]>6:
				# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=1:
						return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=6:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[6]<=1.0:
					# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[10]>1:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[10]<=1:
						return 'True'
					else: return 'True'
				elif obj[6]>1.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>3:
			# {"feature": "Passanger", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Direction_same", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[9]<=0:
					return 'False'
				elif obj[9]>0:
					return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]>3.0:
		return 'False'
	else: return 'False'
