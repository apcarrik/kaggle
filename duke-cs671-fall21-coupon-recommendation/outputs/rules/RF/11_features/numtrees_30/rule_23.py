def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[5]<=17:
		# {"feature": "Age", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[3]>2:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[7]<=2.0:
						return 'True'
					elif obj[7]>2.0:
						return 'False'
					else: return 'False'
				elif obj[4]>1:
					# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1]>0:
						# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[8]>0.0:
							return 'False'
						elif obj[8]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[3]<=2:
			# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[7]<=2.0:
				return 'True'
			elif obj[7]>2.0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[2]<=3:
					return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[5]>17:
		return 'False'
	else: return 'False'
