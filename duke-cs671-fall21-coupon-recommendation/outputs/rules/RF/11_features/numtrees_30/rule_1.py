def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>1:
		# {"feature": "Time", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.7219, "depth": 3}
			if obj[5]>4:
				# {"feature": "Age", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8]<=1.0:
						return 'True'
					elif obj[8]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=4:
				# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]<=2:
						# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1.0:
								return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[4]>2:
						return 'False'
					else: return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[8]>1.0:
				# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>0:
					return 'True'
				elif obj[3]<=0:
					return 'False'
				else: return 'False'
			elif obj[8]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
