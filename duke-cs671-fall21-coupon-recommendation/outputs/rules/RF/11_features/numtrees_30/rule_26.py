def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[3]<=6:
		# {"feature": "Bar", "instances": 31, "metric_value": 0.9812, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[5]<=11:
				# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[7]>1.0:
					# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[8]>1.0:
						return 'True'
					elif obj[8]<=1.0:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]<=0:
							return 'False'
						elif obj[1]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[7]<=1.0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>11:
				return 'True'
			else: return 'True'
		elif obj[6]<=0.0:
			# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[1]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]>2:
							return 'True'
						elif obj[4]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[8]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>6:
		return 'True'
	else: return 'True'
